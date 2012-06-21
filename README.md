## Install:

    pip install travis

## Usage:

    import travis
    repo = travis.show('travis-ci', 'travis-ci')
    print repo.last.stable


## Documentation:

### **repositories ()**

List of the latest Repo()s being tested


### **show (owner, repo, build=None)**

Returns a Repo()

If a build number is provided then a Build() object is returned instead


### **builds (owner, repo)**

Returns a list of Build()s for a given repo


### **Repo (dict())**

* description
* id
* last_build_duration
* last_build_finished_at
* last_build_id
* last_build_language
* last_build_number
* last_build_result
* last_build_started_at
* last_build_status
* public_key
* slug
* builds
* last - *last Build() of the builds list*
* stable - *Build().passed value of the last Build() in builds*


### **Build (dict())**

* branch
* commit
* duration
* event_type
* finished_at
* id
* message
* number
* repository_id
* result
* started_at
* state
* passed - a boolean inverse of the result in value


## *Meant for internal use*
### **get_builds ()**
### **Cute (dict())**


## Bugs & Co.

If you find bugs or new features that are not implemented you can:

 * [Fork and implement the changes](https://github.com/medecau/travis/fork)
 * [Fork and write a test that fails but shouldn't](https://github.com/medecau/travis/fork)
 * [Submit an issue in github](https://github.com/medecau/travis/issues)


## Aknowledgment

[Kenneth Reitz](https://github.com/kennethreitz) for being awesome and showing how to do things right.
