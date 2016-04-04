# Amazing Flask App

[![Build Status](https://travis-ci.org/phips/flask_app.svg?branch=master)](https://travis-ci.org/phips/flask_app)

There is nothing amazing about this app :)

Long story short - it's used in my [Ansible demos](http://github.com/phips/ansible-demos), that's all.

# Using it anyway

    make test
    make run

If you want to make an 'artifact' (read: tarball) then `make dist` will suffice. I tend to do this in a Jenkins job, which my Ansible [deployment demo](https://github.com/phips/ansible-demos/blob/master/roles/app/tasks/deploy.yml#L26) then pulls in.
