# -*- coding: utf-8 -*-

import unittest
import travis

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        pass

    def test_repo_list_without_params(self):
        repos = travis.repositories()
        self.assertEqual(type(repos), type(list()))
        
    def test_repo_list_with_owner(self):
        repos = travis.repositories('travis-ci')
        self.assertEqual(type(repos), type(list()))
    
    def test_repo_list_with_query(self):
        repos = travis.repositories(query='travis-ci')
        self.assertEqual(type(repos), type(list()))
        
    def test_repo_list_with_owner_and_query(self):
        repos = travis.repositories(name='travis-ci', query='travis-ci')
        self.assertEqual(type(repos), type(list()))

    def test_repo(self):
        repo = travis.show('travis-ci', 'travis-ci')
        self.assertEqual(type(repo.stable), type(bool()))

    def test_builds_list(self):
        builds = travis.builds('travis-ci', 'travis-ci')
        self.assertEqual(type(builds), type(list()))

    def test_build(self):
        build = travis.show('travis-ci', 'travis-ci')
        self.assertEqual(type(build.last.passed), type(bool()))
    
    @unittest.skip('not supported any more')
    def test_worker(self):
        workers = travis.workers()
        self.assertEqual(type(workers), type(list()))
    
    def test_jobs(self):
        jobs = travis.jobs('builds.php')
        self.assertEqual(type(jobs), type(list()))
    
    def test_job(self):
        jobs = travis.jobs(job='1680136')
        self.assertEqual(type(jobs), type(travis.Cute({})))
    


if __name__ == '__main__':
    unittest.main()
