# Rasa Haystack Demo



This repo is a bare-bones chat bot project using [Rasa](https://rasa.com/) in combination with [Haystack](https://github.com/deepset-ai/haystack). While Rasa is used for the whole flow of the dialogue and intent management, Haystack is used to answer the long tail of "knowledge queries" that can be answered by searching an answer in a document corpus. This example repo sketches how to use the _fallback intent_ or an dedicated _knowledge base intent_ to offload such queries to haystack.

After initializing a plain rasa project (`rasa init`) changes were made to
- domain.yml
- config.yml 
- data/nlu.yml
- data/rules.yml
- actions/actions.py

More details can be found at [this page](https://haystack.deepset.ai/usage/chatbots)!

## Get Started

- [Install](https://rasa.com/docs/rasa/installation) Rasa
- Start the Haystack REST API and a demo DocumentStore via Docker:
```
git clone https://github.com/deepset-ai/haystack.git
cd haystack
docker-compose pull
docker-compose up
```
   _If you don't use Docker, you can also [install](https://haystack.deepset.ai/overview/get-started) Haystack and start the [Haystack REST API](https://haystack.deepset.ai/usage/rest-api#background-haystack-pipelines) service_  
- Train a model in this repository with `rasa train`  
- Call `rasa shell` to start interacting with the chatbot (alternatively, you can [use Rasa X](https://rasa.com/docs/rasa-x/) and interact with the bot via a developer GUI)  

Our trained model is included in the `models` directory. 
