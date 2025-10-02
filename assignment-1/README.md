
# CPSC 8740 Assignment 1
### Chris Williams, Clemson ID: C11798406, cwill47@clemson.edu

Code available at [chriswil/cpsc8740: Coding Projects for CPSC 8740](https://github.com/chriswil/cpsc8740)

## Setup and Introduction
   
### AI Tools 

I chose to use:
* PyCharm IDE + Claude Code running in Terminal
* Claude Chatbot
* Code Rabbit

### Intro to Tools

#### PyCharm + Claude Code + Claude Chat

I primarily code in Python these days, so I chose the PyCharm IDE which I'm comfortable working with for editing and debugging Python code. I am using Claude Code for code generation and assistance with the 3 apps that we're working on.

For brainstorming possible ideas and thinking ideas of what I'd like to implement with Claude Code, 
I'm using the Claude desktop app for general queries, as well as looking up frameworks and APIs that
Claude Code suggests during implementation.

As you can see in this screenshot, I use the Claude Code command line tool within a Terminal window in PyCharm. I can have a conversation with Claude Code and I can give it access to all of the files in the project so that it can modify files within the project as we're talking through what I want to build. While it is a command line tool, the fact that I can chat with it via the command line and see the code changes in the IDE in real time, it actually has the feel of pair programming. If I need to make slight changes to anything it generates, I can ask Claude to review the code changes and continue working. No need to copy and paste from the Claude Chatbot.

Claude Code can submit pull requests to GitHub, which I can review from Code Rabbit's web interface. I think this will be especially useful as we begin working on larger, more complicated codebases. Rather than remembering the more complicated git actions, I can give Claude the git request in English and as long as I'm clear with my instruction, I found it to be very accurate. Claude will always stop and give you the command that it intends to run, so I'm able to review and approve or reject if my command was misinterpreted.


![PyCharm-ClaudeCode](PyCharm-ClaudeCode.png)


#### [AI Code Reviews | CodeRabbit](https://www.coderabbit.ai/)

I wanted to experiment with automated AI-powered review of the code that Claude Code is generating so I am using Code Rabbit to review pull requests from Claude Code. Claude Code integrates nicely with Github using the GitHub command line program, gh. When I generate a large code change using Claude Code, I can then have it create a pull request on GitHub. Code Rabbit is set up to look at all incoming pull requests on GitHub and will automatically review the code, generating comments on the pull request on GitHub that I can use as a guide for my own review of the code being generated. 

Here's an example of a CodeRabbit review of one of my Claude-generated pull requests, which is visible in my code repo (link is available in the header of this document):

![code-rabbit-pr-review](code-rabbit-pr-review.png)

CodeRabbit currently uses OpenAI's GPT-3.5 and GPT-4, Anthropic's Claude, and Google's Gemini.  


## Experimentation

Our task was to create three apps: a basic calculator, a to-do list application, and a simple tic-tac-toe. I started the process by discussing some ideas with Claude Desktop about what I wanted to build. I wanted something that was easy to package up and run, so web applications were not an option. I worked through several UI alternatives: tkinter, kivy, PyQt, etc. We went through the pros and cons of each option. I decided to go with tkinter due to the ease of use, and the fact that the tkinter library comes with standard Python. Anyone should be able take my scripts and run them successfully, as long as they're working with a relatively recent release of Python. 

Once Claude Chatbot and I came up with a basic plan, I started a session with Claude Code in PyCharm. I captured notes from the Claude Chatbot conversation and copy and pasted relevant portions of that discussion into Claude Code. A best practice for using Claude Code is to have a CLAUDE.md file. This is a special file included in the project that can provide context and instructions for Claude to follow during our conversations.

I discussed how I wanted to:
* keep all code easily portable
* how to structure the files that are generated within my git repo
* have Claude Code manage interactions with the git repo: commits, pull requests, etc.
* integrate with CodeRabbit.ai for automated code reviews

After that conversation was completed, I instructed Claude Code to write the CLAUDE.md file for me and I edited with a few small changes. Then it was time to generate code. This was as simple as instructing Claude to generate the apps that we had been discussing, and to follow the goals present in my CLAUDE.md file. As we went through the process, I had Claude perform various actions on GitHub: committing updates locally, creating pull requests, pushing code to the repository, doing rollbacks if necessary for potential local changes that I wanted to try didn't work as I had hoped. There were a few hiccups with ineffective updates that didn't achieve the goal, but given the organized process that I was trying to follow, it was fairly easy to recover.




## Analysis and Reflection

### Effectiveness of the AI tools

The workflow that I followed for this assignment was very effective I thought. During the planning stages, the Claude desktop app did a very good job of capturing our conversation and summarizing my requirements. I found the code that Claude Code generated was quite accurate and when I reviewed via CodeRabbit, no major problems were ever identified other than code formatting and suggestions for addition of more code comments, which is never a bad suggestion. By my estimate, I think a development project like this would have taken at least 2 to 3 days before, whereas I was able to get something up and running with these AI tools in 2 to 3 hours.


### Reflection - how can these tools be integrated into my workflow? what impact will they have on the future of software development?


My goal going into this was to keep it as organized and well-defined as possible to ensure that I didn't run into any issues with introducing any vague requests into the AI tools that I was using. As we saw with the vibe-coding session that we did in class for 40 minutes, you can quickly get bogged down if you let the tools cycle through your requests and make haphazard code changes without closely monitoring the changes. 

I believe my choice of tools was successful at minimizing a good deal of grunt work that would have greatly slowed me down, such as getting a basic working application up and running with Tkinter. UI work is not a difficult task, but it can be time consuming. I think that capability of getting a quick, working prototype will be very useful in the future as I'm able to get something to demo, and then I will be able to iterate and quickly add new features, and possibly even a more production-quality UI. That ability to skip some of the mundane work and having time to focus more on planning and producing a useful application will have a big impact on the future of software development. 

One thing that especially struck me was how the AI tools that I used, I believe, could have a big impact on the ability of software developers to develop very robust independent code review workflows. The integration of the AI tools, GitHub repo functionality, and the ease in which I could pull in another independent AI tool to help me with the code review process was impressive. Where I might have needed more teammates to help accomplish this, I can now call on AI "agents" to assist me with that part of my software development process.

