# Technologies:
* Azure databricks (Apache Spark) - for data transformation
* Azure datafactory - for data task orchestration
* Azure data lake - for storing data at each transformation step
* Azure synapse - for data warehouse
* Apache Kafka - for stream data processing
* Terraform - for automating setup of azure services

# Insights:
* 
```
# load env variables
client_id = os.environ['REDDIT_CLIENT_ID'] 
client_secret = os.environ['REDDIT_CLIENT_SECRET']
username = os.environ['REDDIT_USERNAME']
password = os.environ['REDDIT_PASSWORD']

redirect_uri = os.environ["REDDIT_REDIRECT_URI"]
duration = "permanent"
state = str(uuid4())

# scopes are needed to explicitly request access to areas of the api
scope = ",".join([
    "identity",
    "edit",
    "flair",
    "history",
    "modconfig",
    "modflair",
    "modlog",
    "modposts",
    "modwiki",
    "mysubreddits",
    "privatemessages",
    "read",
    "report",
    "save",
    "submit",
    "subscribe",
    "vote",
    "wikiedit",
    "wikiread"
])


url = "https://www.reddit.com/api/v1/authorize"
params = {
    "client_id": client_id,
    "response_type": "token",
    "state": state,
    "redirect_uri": redirect_uri,
    "duration": duration,
    "scope": scope
}

response = requests.get(url, params=params)
print(response.json())

# # login to reddit account programmatically with credentials
# # to extract a token that can be used to make requests to the reddit api
# client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
# payload = {
#     "grant_type": "password", 

# }
# headers = {"User-Agent": f"ChangeMeClient/0.1 by {username}"}
# url = "https://www.reddit.com/api/v1/access_token"
# response = requests.post(url, auth=client_auth, data=payload, headers=headers)
# data = response.json()
# token = data['access_token']
# print(token)

# # make sample post to r/test
# url = "https://www.reddit.com/api/submit"
# params = {
#     "sr": "test",
#     "title": "test title from script",
#     "text": "this is a sample text from a python script",
#     "kind": "self"
# }
# url = "https://www.reddit.com/r/Jung/hot"
# params = {
#     "limit": 1
# }
# headers = {
#     "Authorization": f"bearer {token}"
# }
```

* The recommended format for user agent is `<platform>:<app ID>:<version string> (by u/<Reddit username>)`. For example, `android:com.example.myredditapp:v1.2.3 (by u/kemitche)`. `desktop:com.sr-analyses-pipeline:0.1 (by u/<reddit username>)`

* if we don't use our reddit password and username automatically what we can only do with the reddit api is use get requests or read only requests, we can't have permission to write, update, or delete a subreddit, or post, or comment

* Kafka docker images
You've made an excellent analogy, and yes, your understanding is largely correct!

Confluent and Apache Kafka
You are absolutely right. Confluent is essentially a leading provider and steward of Apache Kafka.

Relationship: Confluent was founded by the original creators of Apache Kafka while they were still at LinkedIn. They open-sourced Kafka, and then went on to build Confluent to commercialize and extend Kafka's capabilities.


What Confluent provides:

Managed Service (Confluent Cloud): This is their flagship offering, a fully managed, cloud-native service for Apache Kafka. You don't have to worry about setting up, scaling, patching, or maintaining Kafka clusters; Confluent handles all of that. This is very similar to how you use a managed service in Azure (like Azure Event Hubs) or AWS (like Amazon MSK for Kafka).

Enterprise Distribution (Confluent Platform): They offer an enhanced, production-ready distribution of Kafka that includes additional features, management tools, security enhancements, and connectors that go beyond the open-source Apache Kafka project. You can run this on your own infrastructure.

Development & Contributions: Confluent is a major contributor to the open-source Apache Kafka project, continuously driving its development and adding new features.

Bitnami and Apache Spark
Your analogy with Bitnami is very apt.

Relationship: Bitnami isn't the creator of Apache Spark, but they are a very popular distributor and packager of Apache Spark (and many other open-source applications).

What Bitnami provides: They take the open-source Apache Spark software and create pre-configured, optimized, and easy-to-deploy images (like Docker images, Helm charts for Kubernetes, or virtual machine images). This makes it much simpler for users to get Spark up and running quickly without dealing with complex installation and configuration. They manage the packaging, versioning, and often the security patching of these images.

The Analogy Holds:
The core similarity is that both Confluent and Bitnami provide ways to simplify the deployment, management, and use of complex open-source software (Kafka and Spark, respectively).

Confluent manages Apache Kafka, offering both a fully hosted "Kafka as a Service" (Confluent Cloud) and an enhanced enterprise package (Confluent Platform). They are deeply integrated with the development of Kafka itself.

Bitnami manages Apache Spark by providing pre-built, ready-to-run packages/images, reducing the operational burden of setting it up yourself in various environments like Docker.

So, yes, if Bitnami "manages" the deployment and packaging of Apache Spark, then Confluent definitely "manages" Apache Kafka, and then some, extending into full managed service offerings and enterprise-grade features.

oh so that's why some docker images aren't directly named apache kafka, its always bitnami/kafka, apache/kafka, or the image owned by confluent confluentinc/cp-kafka. I mean judging by the names it would seem more intuitive to pick the apache/kafka image? Why do people use confluentinc/cp-kakfa image frequently rather than the other ones? What's the difference anyway?

You've hit on a really common observation when working with Docker images for popular open-source projects! It can definitely be confusing why there are multiple "official-looking" images.

Let's break down the differences between apache/kafka, bitnami/kafka, and confluentinc/cp-kafka and why confluentinc/cp-kafka is often preferred.

The Different Kafka Docker Images:
apache/kafka (The "Official" Apache Project Image)

Origin: This image is maintained by the Apache Kafka project itself. It's often found in the docker.io/apache namespace.

What it contains: It typically contains the vanilla, bare-bones Apache Kafka broker software (and sometimes ZooKeeper, depending on the version/tag). It's built directly from the Apache Kafka source code.

Purpose: To provide a pure, unmodified Apache Kafka experience.

Usability: Can be a bit more challenging for beginners to set up, especially for multi-broker clusters or when integrating with other tools, as it might require more manual configuration or additional scripts. It's often focused on providing just the core Kafka.

bitnami/kafka (Bitnami's Managed Image)

Origin: Maintained by Bitnami (now part of VMware/Broadcom), a company known for packaging open-source software.

What it contains: This image also contains Apache Kafka, but it's often built with additional optimizations, robust configurations, and sometimes helper scripts to make it easier to deploy and manage in common environments (like Kubernetes using Helm charts). They focus on secure and production-ready defaults.

Purpose: To provide highly opinionated, ready-to-run, and well-maintained images for easy deployment of open-source applications.

Usability: Generally considered more user-friendly for getting started quickly and for production deployments, due to built-in helper scripts and sensible defaults.

confluentinc/cp-kafka (Confluent Platform Kafka Image)

Origin: Maintained by Confluent, the company founded by Kafka's original creators.

What it contains: This image contains the Apache Kafka broker plus components from the Confluent Platform. The Confluent Platform is an enterprise-grade distribution that extends Apache Kafka with additional features like:

Confluent Control Center: A web-based UI for monitoring and managing Kafka.

Schema Registry: Essential for enforcing data schema compatibility in Kafka topics.

Kafka Connect: For building connectors to other systems, often with more robust features or managed connectors.

KSQL (now ksqlDB): A SQL interface for real-time stream processing.

Security features: Enhanced authentication/authorization.

Purpose: To provide a comprehensive, integrated ecosystem around Kafka for enterprise use cases, going beyond just the basic broker.

Usability: Very powerful for building full-fledged Kafka-based data platforms, but it brings the entire Confluent ecosystem, which might be overkill for very simple use cases if you only need the broker.

Why confluentinc/cp-kafka is Frequently Used (and Often Preferred):
Even if you're not paying for Confluent's enterprise support, their Docker images are very popular for several reasons:

Completeness & Ecosystem: For many real-world use cases, you don't just need the Kafka broker; you need Schema Registry, Kafka Connect, and robust monitoring. The confluentinc/cp-kafka images (and others in the confluentinc namespace like cp-schema-registry, cp-kafka-connect) provide a pre-packaged, compatible, and well-tested way to deploy this entire ecosystem. It simplifies setup greatly compared to getting each component separately.

Expertise & Maintenance: Confluent is the commercial entity most deeply involved with Kafka's development. Their images are generally very well-maintained, kept up-to-date with the latest Kafka versions, and often include performance optimizations or critical bug fixes that might take longer to appear in community-maintained "official" images.

Production Readiness: Confluent's focus is on enterprise deployments. Their images are often designed with production best practices in mind, including sensible default configurations, logging, and metrics.

Documentation & Community: Confluent has extensive documentation and a large community around their platform, making it easier to troubleshoot and find examples.

In summary, while apache/kafka gives you the pure open-source core, bitnami/kafka offers a streamlined, well-packaged version of that core. confluentinc/cp-kafka provides the core Kafka broker plus a powerful, integrated suite of tools and features from the Confluent Platform, making it a highly attractive option for developers and organizations building comprehensive data streaming solutions. People choose it because it often saves significant time and effort in integrating and managing the broader Kafka ecosystem.

* 
You're asking a fantastic question that gets to the heart of real-time data processing and why Kafka is so powerful! Your assumptions are good starting points, but let's refine them.

Batch Processing vs. Streaming Processing (The Core Difference)
Imagine you have a stack of mail:

Batch Processing: Is like waiting for all your mail to arrive at the end of the day or week, then opening it all at once and dealing with it. You process it in big "batches." This is good for things that don't need immediate action, like monthly billing.

Streaming Processing: Is like having a special delivery person who brings each piece of mail to you the second it arrives. You open and deal with it immediately. This is crucial for things that need instant responses, like fraud detection, live dashboards, or real-time recommendations.

How Apache Kafka Works (The "Central Nervous System" for Streaming Data)
Apache Kafka is like a super-efficient, highly reliable "postal service" or "messaging highway" designed specifically for real-time events. It doesn't just call APIs over and over; it acts as a central hub where data is constantly flowing, being sent by some and picked up by others.


Here's how its main parts fit together:

Events/Messages:

This is the smallest unit of data flowing through Kafka. Think of it as a single piece of information, like "User X clicked on Product Y," "Customer Z made a payment," or "Temperature sensor A read 25°C."

Topics (The "Categories" or "Channels"):

Imagine a Kafka system has many different "categories" or "channels" for different types of events. These are called Topics.

For example, you might have a user_clicks topic, a payments topic, or a sensor_readings topic.

When an event happens, it's sent to the relevant topic.

Producers (The "Data Senders"):

These are applications or systems that generate data and send it into Kafka.

They are like the people writing and mailing letters.

Example (Reddit Data): Your Python script reading from the Reddit API would be a Producer. It takes new Reddit posts/comments and "produces" them as events to a reddit_posts topic in Kafka.

Consumers (The "Data Receivers"):

These are applications or systems that read data from Kafka.

They are like the people who pick up mail from their mailbox.

Crucially: Multiple Consumers can read from the same topic independently, at their own pace, without affecting each other. One might be building a dashboard, another might be analyzing sentiment, and another might be storing data in a database.

Example (Transformation): Your Azure Databricks Spark job would be a Consumer. It continuously reads new Reddit posts from the reddit_posts topic to transform them.

Brokers (The "Mail Sorting & Storage Hubs"):

These are the actual servers that make up the Kafka system. A group of Brokers is called a Kafka cluster.

What they do:

When a Producer sends an event to a Topic, the Broker receives it and stores it reliably (writes it to disk). This is key – Kafka doesn't just forward; it stores.

They keep events for a configurable amount of time (e.g., 7 days, 30 days). This means Consumers don't have to be online all the time to catch every event; they can read from where they left off.

They manage which events go to which topics and handle requests from Consumers to read from specific parts of a topic.

They ensure high availability and fault tolerance: if one Broker goes down, others take over.

Why Kafka is Used for Real-Time Streaming (and not just repeatedly calling APIs):
You're right that streaming APIs give out data constantly. Kafka doesn't call an API over and over; it receives data from APIs (via Producers) and acts as a central, high-throughput, fault-tolerant buffer and distribution system.

Decoupling (The Main Reason):

Kafka acts as a buffer and mediator between systems. The Producer (e.g., your Reddit script) doesn't need to know who will use the data or how many systems will consume it. It just "publishes" to a topic.

The Consumers (e.g., Databricks, a dashboard, a database) don't need to know where the data came from. They just "subscribe" to a topic.

This "decoupling" is huge. You can add new Consumers or change existing ones without affecting the Producer, and vice versa. In traditional direct API calls, if the API endpoint or the consuming system changes, everything might break.

Scalability: Kafka can handle millions of events per second. It's built for very high throughput.

Durability: Events are stored on disk by Brokers, so even if a Consumer goes down, it won't miss data; it can pick up from where it left off when it comes back online.

Fault Tolerance: It's designed to be highly available. If a server (Broker) fails, the data is still accessible from other Brokers.

Replayability: Because data is stored for a period, Consumers can "go back in time" and re-process old events if needed (e.g., for testing new logic or recovering from an error).

So, in essence, Kafka is the robust, scalable, and reliable pipeline that ensures real-time data flows smoothly and continuously from where it's generated to wherever it needs to be pro-essed or analyzed, acting as a central, persistent message bus rather than just a repetitive API caller.

so in a sense this is what it looks like: producer (python script calling an API reddit, news, medium) -> kafka broker <- consumer (dash board, apache spark, data warehouse, database). And that a kafka broker consists of multiple topics/categories, and each in category there is an event of the similar category, and that multiple kafka brokers are part of a kafka cluster?

# Articles, Videos, Papers:
* using reddit api using python wrapper praw: https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
* creating a client secret and id for reddit api: https://github.com/reddit-archive/reddit/wiki/OAuth2
* examples on using oauth2 for reddit api: https://github.com/reddit-archive/reddit/wiki/OAuth2-Python-Example
* news api for real time news: https://newsapi.org/docs
* public data streaming apis: https://github.com/bytewax/awesome-public-real-time-datasets
* public apis: https://github.com/public-apis/public-apis