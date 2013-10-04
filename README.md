relayr
======

This project is designed to be used offline, to capture and then later replay requests for integration tests.

Built out of the need to play with WebHooks in an environment that is not publicly accessible. 

While github recommends using requestb.in, its json visualization is lacking and sometimes the full request does not show, which is infuriating.

## Dependencies

* flask (web)
* RethinkDB (storage)
