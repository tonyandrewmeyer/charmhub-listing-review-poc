# How to request a review for charm for being listed on charmhub.io?

Reviewing charms encourages the involvement of the community. The community refers to individuals and organisations creating or contributing to charms, Juju and the wider charming ecosystem. The goals of the review are:

1. Be transparent about the capabilities and qualities of a charm.
2. Ensure a common level of quality.

A listing review is *not* code review. The reviewer may be looking at some of the charm code, and may have comments on it, but the listing review is not a review of the architecture or design of the charm, and is not a line-by-line review of the charm code.

## Key considerations

1. The process is streamlined: The party requesting the review provides structured evidence as input to the review process.
2. A review is transparent for the community. Review and the review comments are public.
3. Everyone can participate in the review, for example, participate in a discussion in a GitHub issue. A review may benefit from the expertise of a reviewer in the relevant field. Thus, the review process is flexible and open to involving multiple persons.
4. The review covers the effective automation of tests for automated approvals of subsequent releases.

## Steps of a review

The specification provides details and summaries of how the review works. However, the overall approach is straightforward:

1. The author requests a review for *one* charm at a time with all prerequisites using a [listing request issue](https://github.com/tonyandrewmeyer/charmhub-listing-review/issues/new) in this repository.
2. The reviewer checks if the prerequisites are met and the pull request is ready.
3. The public review is carried out as a conversation on the pull request.
4. The review concludes if the charm is 'publication ready'.
5. If the review is at least 'publication-ready', the store team is asked to list the charm.

The result of the process is that:
* if the review is successful, the charm is switched to listed mode, or
* if the review is unsuccessful, the charm does not reach the required criteria and the charm remains unlisted, until the issues are resolved.

## Roles and concepts

|Role or item|Description|
| --- | --- |
|Author|Author of the charm or person representing the organisation. The person submitting the charm for review is called the author in this document.|
|Publisher|The responsible person or organisation for publishing the charm.|
|Review group|A group of contact persons watching for review requests to arrive and requesting modifications or assigning a review to a suitable reviewer. This is currently the Canonical Charm Tech team.|
|Reviewer|Person conducting the review.|
|Listing|After the reviewer has reviewed the charm successfully, it can be switched to 'listing'. Listing means that the charm will be part of the search result when querying the Web pages and API of Charmhub.io. Without 'listing', the charm will be available under its URL but is not listed in searches.|

The charm listing criteria consists of:

* A set of automated checks (for example: is there a license file?)
* A set of manual checks, which are shown in a checklist in the issue
* Reviewing the charm against current charming best practices, which are automatically collated from the charming ecosystem documentation and also included in a checklist in the issue

## Review prerequisites

The process has the following prerequisites to be delivered by the author. The issue template for a listing request will prompt the author for this information:

1. The charm source code is accessible for reviewers and an URL to a (git) source code repository is available.
2. Information for the reviewer to verify that the charm behaves as expected - in simple cases, a tutorial is a good method for this. In more complex cases, and particularly when specific resources are required, a demo call or video is a better choice.
3. URLs for CI workflows and specific documentation.
4. Publisher details.

# Get started

If the charm is ready for review, [open an issue in this repository](https://github.com/tonyandrewmeyer/charmhub-listing-review/issues/new).





TODO: Something like this needs to go into the charmcraft docs, with a link to the new process, once everything is complete & ready.

## Requirements for public listing

Everyone can publish charms to [https://charmhub.io/](https://charmhub.io/). Then, the charm can be accessed for deployments using Juju or via a web browser by its URL. If a charm is published in Charmhub.io and included in search results, the charm entry needs to be switched into the listed mode. To bring your charm into the listing, [reach out to the community](https://discourse.charmhub.io/c/charmhub-requests/46) to announce your charm and ask for a review by an experienced community member.
