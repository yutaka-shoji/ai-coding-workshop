# AI Coding Workshop

This repository is designed for an AI coding workshop using GitHub Copilot and Roo Code.

## Workshop Overview

Learn how to effectively utilize AI coding assistance tools using Python.

## Requirements

- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/): Code editor
- [GitHub Copilot subscription](https://github.com/features/copilot): AI coding assistant service (requires GitHub account)
    - [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) (vscode extension)
    - [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) (vscode extension)
- [Roo Code](https://github.com/RooVetGit/Roo-Code) (vscode extension): AI coding agent extension
- [uv](https://docs.astral.sh/uv/): Python package manager

### Optional

- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (vscode extension): Python Language Server (type check)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) (vscode extension): Python Linter and Formatter
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) (vscode extension): Show errors inline
- [Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) (vscode extension): AI Agent alternative (VS Code Extension)

## Workshop Agenda (1.5 hours)

### 1. Introduction (10 minutes)
- Workshop objectives and goals
- Overview of AI coding tools
- Today's agenda

### 2. Environment Setup (10 minutes)
- Sample repository preparation
- Python environment verification
- VS Code extension installation check

### 3. GitHub Copilot Hands-on (10 minutes)
1. Basic Code Completion (5 minutes)
2. Chat mode (5 minutes)

### 4. Roo Code Hands-on (45 minutes)
1. Roo Code Overview and Setup (10 minutes)
2. Have Roo implement from scratch (20 minutes)
3. Roo's code analysis (10 minutes)
4. Summary and advanced tips (5 minutes)

#### 5. Paper Survey with Roo Code (5 minutes)

https://github.com/yutaka-shoji/surveyor

- Example of using Roo Code for paper survey

### 6. Q&A, Discussion (10 minutes)
- Participant questions
- Workshop review

## Flow Chart

```mermaid
graph TD
    A["Introduction (10min)"] --> B{"Environment Setup (10min)"};
    B --> C["GitHub Copilot Hands-on (10min)"];
    C --> D["Roo Code Hands-on (40min)"];
    D --> E["Paper Survey with Roo Code (10min)"];
    E --> F["Q&A and Wrap-up (10min)"];

    subgraph C [GitHub Copilot Hands-on]
        C1["Basic Code Completion (5min)"]
        C2["Chat mode (5min)"]
    end

    subgraph D [Roo Code Hands-on]
        E1["Roo Code Overview and Setup (10min)"]
        E2["Text Place Holder (15min)"]
        E3["Text Place Holder (15min)"]
    end
```