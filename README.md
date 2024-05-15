# LLMOPs with Azure Machine Learning

**_Note: In order to most efficiently utilize GitHub actions please FORK the repository as opposed to cloning_**

### **Overview**
This is a starting guide designed to accelerate the development of a robust LLMOPs framework with Microsoft Azure.

The repository aligns with the three main pillars of LLMOps:
1. Evaluation/Testing - _pre-deployment processes to provide confidence for release to end users_
2. Monitoring - _near real-time capture of deployment metrics and security threats_
3. Feedback - _post-interaction analysis of user behavior and model responses to drive future improvements_

Checkout this Blog post for a more in depth overview: [Is my LLM Chatbot Ready for Production?](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/is-my-llm-chatbot-ready-for-production/ba-p/4102526)

### **Getting Started**  
This repository contains Demo Notebooks with accompanying [source code](./src/) for all stages of an LLMOps implementaiton
  
- **Demo Notebooks:** Step-by-Step interactive walkthroughs of various eval techniques
  - 00_setup: _Environment and development setup_
  - 01_evaluation: _Use PromptFlow to orchestrate evaluation of a chatbot. Then use that evaluation framework with GitHub Actions for CI/CD_
  - 02_monitoring: _Setup a system to monitor a chatbot for secutiry and availability in real time_
  - 03_feedback: _Evaluate production inputs/responses captured with Model Data Collector. Use an LLM to sythesize and categorize mock [user survey feedback](./data/sample_user_feedback.csv)_


