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




Add some of this?

##### Contact and URLs


| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
|The charm homepage provides links that are important to the user. Interested developers should be able to contact the charming project and directions on where and how to submit questions and issues must be provided.| URLs must be provided to enable collaboration and exchange on the charm, ideally as metadata on Charmhub.<br/>A best practice is to have an issue template configured for the issue tracker! (Example see, e.g., [alertmanager-k8s issue template](https://github.com/canonical/alertmanager-k8s-operator/issues/new/choose))<br/>The homepage should point to the source code repository, providing an entry point to charm development and contributions.<br/> :warning: Further support is coming for the distinct identification of the project homepage, source code repository and issue tracker in charm metadata, and on Charmhub.|

##### Community discussions

| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| A Discourse link or Mattermost channel must be available for discussion, announcements and the exchange of ideas, as well as anything else which would not fit into an issue.<p>For the application, links to the referring forums can also be provided. | Discourse is preferred because framework topics and other charms are also discussed there. It is the most popular place for the community of charms. Therefore, technical questions are most likely covered there.<p> Issues can also be discussed in the [public chat](https://matrix.to/#/#charmhub-juju:ubuntu.com).






Stage 2

#### The charm has sensible defaults

A user can deploy the charm with a sensible default configuration.

| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| The purpose is to provide a fast and reliable entry point for evaluation. Of course, optimised deployments will require configurations.  |  Often applications require initial passwords to be set, which should be auto-generated and retrievable using an action or {ref}`secrets <secret>`. <p> Hostnames and load balancer addresses are examples that often cannot be set with a sensible default. But they should be covered in the documentation and indicated clearly in the status messages on deployment when not properly set.|

#### The charm is compatible with the ecosystem

The charm can expose provides/requires interfaces for integration ready to be adopted by the ecosystem.

| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Newly proposed relations have been reviewed and approved by experts to ensure:<p>&#8226; The relation is ready for adoption by other charmers from a development best practice point of view.<p>&#8226;  No conflicts with existing relations of published charms.<p>&#8226;  Relation naming and structuring are consistent with existing relations.<p>&#8226; Tests cover integration with the applications consuming the relations. | A [Github project](https://github.com/canonical/charm-relation-interfaces) structures and defines the implementation of relations.<p>No new relation should conflict with the ones covered by the relation integration set [published on Github](https://github.com/canonical/charm-relation-interfaces).<p>&#8226; See more: [Charmcraft | Manage relations](https://canonical-charmcraft.readthedocs-hosted.com/stable/howto/manage-charms/#manage-relations), [Ops | Manage relations](https://ops.readthedocs.io/en/latest/howto/manage-relations.html)|

#### The charm upgrades the application safely

The charm supports upgrading the workload and the application. An upgrade task preserves data and settings of both.

| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| A best practice is to support upgrades sequentially, meaning that users of the charm can regularly apply upgrades in the sequence of released revisions. | &#8226; {ref}`upgrade-an-application`|

#### The charm supports scaling up and down
**If the application permits or supports it,** the charm does not only scale up but also supports scaling down.

| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Scale-up and scale-down can involve the number of deployment units and the allocated resources (such as storage or computing). | <p>&#8226;  {ref}`scale-an-application` <p>Note that the cited links also point to how to deal with relations when instances are added or removed:<p>&#8226; See more: [Charmcraft | Manage relations](https://canonical-charmcraft.readthedocs-hosted.com/stable/howto/manage-charms/#manage-relations), [Ops | Manage relations](https://ops.readthedocs.io/en/latest/howto/manage-relations.html) |
<!--
<a href="#heading--backup"><h2 id="heading--backup">The charm supports backup and restore</h2></a>

**If the application supports it,** the charm should be recoverable to a working state after a unit is redeployed, migrated, or lost, and a backup copy of the workload's state is attached.

| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| As a best practice, charms…<p>&#8226; … are as stateless as possible (or just stateless), and<p>&#8226; … store in a storage that can be backed up.<p> If the application provides backup functionality already, the charm uses this functionality. | Consider [this example](https://...) as an example of backup operations to be covered. |
-->

#### The charm is integrated with observability

Engineers and administrators who operate an application at a production-grade level need to capture and interpret the application’s state.

| Objectives  | Tips, examples, further reading |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Integrating observability refers to providing:<p>&#8226; a metrics endpoint,<p>&#8226; alert rules,<p>&#8226; Grafana dashboards, and<p>&#8226; integration with a log sink (e.g. [Loki](https://charmhub.io/loki-k8s)).| Consider the [Canonical Observability Stack](https://charmhub.io/topics/canonical-observability-stack) (COS) for covering observability in charms. Several endpoints are available from the COS to integrate with charms:<p>&#8226; Provide metrics endpoints using the MetricsProviderEndpoint<p>&#8226; Provide alert rules to Prometheus<p>&#8226; Provide dashboards using the GrafanaDashboardProvider<p>&#8226; Require a logging endpoint using the LogProxyConsumer or LokiPushApiConsumer<p>More information is available on the [Canonical Observability Stack homepage](https://charmhub.io/topics/canonical-observability-stack).<p>Consider the Zinc charm implementation as [an example for integrations with Prometheus, Grafana and Loki](https://github.com/jnsgruk/zinc-k8s-operator/blob/main/charmcraft.yaml). |




Something like this needs to go into the charmcraft docs, with a link to the new process, once everything is complete & ready.

## Requirements for public listing

Everyone can publish charms to [https://charmhub.io/](https://charmhub.io/). Then, the charm can be accessed for deployments using Juju or via a web browser by its URL. If a charm is published in Charmhub.io and included in search results, the charm entry needs to be switched into the listed mode. To bring your charm into the listing, [reach out to the community](https://discourse.charmhub.io/c/charmhub-requests/46) to announce your charm and ask for a review by an experienced community member.
