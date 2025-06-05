#! /usr/bin/env python

def issue():
    summary = f"Review {project['name']}"

def issue_description():
    return f"""
Please review the charm by checking each of the items in the following checklist.

If you find other improvements or fixes that could be made to the charm, feel free
to suggest those, but **they do not block listing**. If you find something that's
missing from the review checklist or best practices, please separately suggest that
[add instructions on how] so that we can keep the review process consistent.

When reviewing test coverage of the charm, note that:

* Unit tests are recommended, but not required.
* A minimal set of integration tests is required, as outlined in the checklist.
* There is no minimum for test coverage. We suggest that tests cover at least all
  configuration options and actions, as well as the observed Juju events, but
  this is not a requirement for listing.
* Some charms may have additional tests in an external location, particularly if
  the charm has specific resource requirements (such as specific hardware).

TODO: add something about if this has a charm lib then also check x,y,z, ask James
for a list perhaps.

Please provide your review within *three working days*. If blocking issues are found,
please help the submitter work through those, and respond to any follow-up posts within
*one working day*.

## Listing requirements

* [ ] The charm does what it is meant to do, per the [demo]({project['demo']})
* [ ] The [charm's page on Charmhub](https://charmhub.io/{project['name']}) provides
  a quality impression. The overall appearance looks good and the documentation looks
  reasonable.
* [ ] [Automated releasing]({ci['release']}) to unstable channels exists
* [ ] [Integration tests]({ci['integration']}) exist, are run on every change to the
  main branch, and are passing. At minimum, the tests verify that the charm can be
  deployed and ends up in a success state, and that the charm can be integrated with
  at least one example for each 'provides' and 'requires' specified (including
  optional, excluding tracing) ending up in a success state. The tests should be
  run with `charmcraft test`
""".strip()
