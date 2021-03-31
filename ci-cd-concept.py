1) Countinuos Intigration = countinuos build + countinuos testing


2) CI/CD PIPELINE
    i)    Dev Push code (git, bitbucket) -> response return to dev
    ii)   Build                          -> response return to dev
    iii)  Unit Test                      -> response return to dev   
    iv)   Deploy                         -> response return to dev
    v)    Staging/Prod Server Deplo      -> response return to dev
    vi)   Measure & Validation (QA Test) -> response return to dev


3) CI/CD PROCESS
    i)    PLAN                           -> git, bitbucket
    ii)   CODE                           -> git, bitbucket
    iii)  BUILD                          -> maven, gradie
          (a) code compile (b) code review (c) unit testing (d) integration testing (e) packaging (.jar, .war)

    iv)   TEST                           -> selenium, J-unit   

    v)    DEPLOY                         -> chef, puppet
    vi)   OPERATE                        -> chef, puppet
    vii)  MONITOR                        -> nagios