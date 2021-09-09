# Rasa Haystack Demo



This repo is a bare-bones chat bot project using [Rasa](https://rasa.com/) that is set up to communicate with a running [Haystack](https://github.com/deepset-ai/haystack) neural question answering service. 

After initializing the project (`rasa init`) changes were made to
- domain.yml
- config.yml 
- data/nlu.yml
- data/rules.yml
- actions/actions.py

More details can be found at [this page](https://haystack.deepset.ai/usage/chatbots)!

## Get Started

- [Install](https://rasa.com/docs/rasa/installation) Rasa
- [Install](https://github.com/deepset-ai/haystack) Haystack
- Start a [Haystack REST API](https://haystack.deepset.ai/usage/rest-api#background-haystack-pipelines) service
- Train a model in this repository with `rasa train`
- Call `rasa shell` to start interacting with the chatbot (alternatively, you can [use Rasa X](https://rasa.com/docs/rasa-x/) and interact with the bot via a developer GUI)

Our trained model is included in the `models` directory. 
