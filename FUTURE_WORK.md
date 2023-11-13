# Future Work

## Feature Flag Integration

### Introduction
Feature flags, also known as feature toggles, are tools that enable teams to activate or deactivate specific features in an application without redeploying code. 

### Why it matters
- It empowers engineering teams to manage the availability or presentation of features efficiently.

- It enables progressive delivery.

- It mitigates the risks quickly. 

- It enables the user centric development via customized soutions provided to target groups of users.

### Existing solutions

There are lots of tools in market could handle both the simple and complex use cases.
- [ConfigCat](https://configcat.com/)
- [LaunchDarkly](https://launchdarkly.com/) 
- [Split](https://www.split.io/). 

## Interactive Mode Option

### Introduction
CLI Interactive mode (or interactive prompting) is a feature where the program or script prompts the user for input during runtime, typically in a conversational manner.

### Why it matters
 - Interactive prompting makes CLI more user-friendly for users who find it challenging remembering all required options.

- Interactive prompting reduced the chances of errors when providing all required parameters.

- Interactive prompting empowers dynamic and context-aware user experience.

### Tools available in the market
Typer already support this functionality. Check out [here](https://typer.tiangolo.com/tutorial/prompt/) for detail information.

## Configuration Management
Allow users to configure the CLI tool using a configuration file

### Introduction
Allow users to configure the CLI tool using a configuration file.

### Why it matters
- Users can tailor the behavior of the CLI tool to suit their specific needs and preferences.

- Configuration files provide a consistent and standardized way for users to set options and parameters rather than error-prone manual input

- Configuration files are typically easier to read and understand than command-line arguments, especially when dealing with a large number of options

### Tools available in the market
The configuration file could be Json, Yaml file.
- PyYAML for reading yaml file
- Python's default `json` module for reading json file

## Observeability

### Introduction
It is the ability to understand and gain insights into the internal workings of a system based on the external outputs or behaviors it exhibits.

### Why it matters
- Monitor the performance of your CLI program ran in other hosts in real-time. 

- Efficient error tracking for quickly identifying and fixing issues to improve the reliability of your CLI tool.

- Empowers the user experience improvement via insights collected via observability tools.

- Enable logging and auditing to understand user actions and troubleshoot issues.

### Tools available in the market
- Datadog 

- New Relic

- Sentry

- OpenTelemetry

## Dockerization

### Introduction
It is the process of packaging and deploying applications, along with their dependencies and runtime environments, into lightweight, portable containers using Docker

### Why it matters
- This ensures a consistent environment across different development machines and deployment targets, reducing the "it works on my machine" problem.

- Docker containers provide isolation for the CLI tool, preventing it from interfering with the host system or other applications.

- Docker enables reproducibility via defining the entire environment, including dependencies and configurations, using a Dockerfile. 

### Tools available in the market
We just need Docker installed and created relevant dockerfile.

## Localization

### Introduction
The process of adapting a product, service, or content to meet the linguistic, cultural, and functional requirements of a specific locale or target audience.

### Why it matters
- Localization can help increase the tool's adoption and usability in diverse environments

- Localization makes CLI tools accessible to a broader audience by providing support for multiple languages.

- Different regions have varying measurement units. Localizing a CLI tool ensures that measurement units align with the conventions and expectations of users in specific regions.

### Tools available in the market
- Python's `gettext` module is a popular choice for internationalizing Python programs.

- `Babel` is a comprehensive library that supports internationalization and localization in Python
