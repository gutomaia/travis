# -*- coding: utf-8 -*-

import requests
from json import dumps

SLUG = "%s/%s"
REPOS = "http://travis-ci.org/repositories.json"
REPO = "http://travis-ci.org/%s/%s.json"
BUILDS = "http://travis-ci.org/%s/builds.json"
BUILD = "http://travis-ci.org/%s/%s/%s.json"
WORKERS = "http://travis-ci.org/workers.json"
JOBS = "http://travis-ci.org/jobs.json"
JOB = "http://travis-ci.org/jobs/%s.json"

class Cute(object):
    """
        Base class to create objects from request().json
    """
    def __init__(self, d):
        self.d = d
        for k,v in d.items():
            if type(v) == type(dict):
                setattr(self, k, Cute(v)) # cute dictionaries
            elif type(v) == type(list):
                setattr(self, k, [Cute(x) for x in v]) # cute lists
            else:
                setattr(self, k, v)
    
    @property
    def cute(self):
        return dumps(self.d, 2)

class Repo(Cute):
    """
        The representation of a repository
    """
    def __repr__(self):
        return self.slug
    
    @property
    def builds(self):
        return get_builds(self.slug)
    
    @property
    def last(self):
        return self.builds[-1]
    
    @property
    def stable(self):
        return not self.last.result


class  Build(Cute):
    """
        The representation of a Build()
    """
    @property
    def passed(self):
        return not self.result

class  Worker(Cute):
    """
        The representation of a Worker()
    """
    @property
    def ready(self):
        return self.state == 'ready'

def repositories(name=None, query=None):
    """
        A list of Repo()s
    """
    if name or query:
        r = request(REPOS, params={'owner_name':name, 'search':query})
    else:
        r = request(REPOS)
    repos=list()
    for repo in r.json:
        repos.append(Repo(repo))
    return repos

def show(owner, repo, build=None):
    """
        Returns a Repo() or build depending on what you want
    """
    if build:
        return Build(request(BUILD % (owner, repo, build)).json)
    else:
        return Repo(request(REPO % (owner, repo)).json)

def builds(owner, repo):
    """
        A list of Build()s
    """
    return get_builds('%s/%s' % (owner, repo))

def get_builds(slug):
    r = request(BUILDS % slug)
    builds=list()
    for build in r.json:
        builds.append(Build(build))
    return builds

def workers():
    r = request(WORKERS)
    workers = list()
    for w in r.json:
        workers.append(Cute(w))
    return workers

def jobs(queue=None, job=None):
    if job:
        r = request(JOB % job)
        return Cute(r.json)
    elif queue:
        r = request(JOBS, params={'queue': queue})
        jobs = list()
        for w in r.json:
            jobs.append(Cute(w))
        return jobs
    

def request(url, params=None):
    """
        Returns a request object with some parameters set for all requests
    """
    r = requests.get(url, params=params, allow_redirects=False)
    if r.ok:
        return r
    else:
        # RAISE HELL
        pass

