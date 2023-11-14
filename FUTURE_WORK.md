# Future Work

## Feature Flag Integration

### Introduction
Feature flags, also known as feature toggles, are tools that enable teams to activate or deactivate specific features in an application without redeploying code. 

### Why it matters
- It empowers engineering teams to manage the availability or presentation of features efficiently.

- It enables progressive delivery.

- It mitigates the risks quickly. 

- It enables the user-centric development via customized solutions provided to target groups of users.

### Existing solutions

There are lots of tools in the market that could handle both simple and complex use cases.
- [ConfigCat](https://configcat.com/)
- [LaunchDarkly](https://launchdarkly.com/) 
- [Split](https://www.split.io/)

## Interactive Mode Option

### Introduction
CLI Interactive mode (or interactive prompting) is a feature where the program or script prompts the user for input during runtime, typically in a conversational manner.

### Why it matters
 - Interactive prompting makes CLI more user-friendly for users who find it challenging to remember all required options.

- Interactive prompting reduced the chances of errors when providing all required parameters.

- Interactive prompting empowers dynamic and context-aware user experience.

### Tools available in the market
Typer already supports this functionality. Check out [here](https://typer.tiangolo.com/tutorial/prompt/) for detailed information.

## Configuration Management

### Introduction
Allow users to configure the CLI tool using an external configuration file.

### Why it matters
- Users can tailor the behavior of the CLI tool to suit their specific needs and preferences.

- Configuration files provide a consistent and standardized way for users to set options and parameters rather than error-prone manual input

- Configuration files are typically easier to read and understand than command-line arguments, especially when dealing with a large number of options.

### Tools available in the market
The configuration file could be JSON or Yaml file.
- [PyYAML](https://pypi.org/project/PyYAML/) for reading yaml file.
- Python's default [json](https://docs.python.org/3/library/json.html) module for reading json file.

## Observeability

### Introduction
It is the ability to understand and gain insights into the internal workings of a system based on the external outputs or behaviors it exhibits.

### Why it matters
- Monitor the performance of your CLI program run in other hosts in real-time. 

- Efficient error tracking for quickly identifying and fixing issues to improve the reliability of your CLI tool.

- Empowers the user experience improvement via insights collected via observability tools.

- Enable logging and auditing to understand user actions and troubleshoot issues.

### Tools available in the market
- [Datadog](https://www.datadoghq.com/) 

- [New Relic](https://newrelic.com/)

- [Sentry](https://sentry.io/welcome/)

- [OpenTelemetry](https://opentelemetry.io/)

## Dockerization

### Introduction
It is the process of packaging and deploying applications, along with their dependencies and runtime environments, into lightweight, portable containers using [Docker](https://www.docker.com/)

### Why it matters
- This ensures a consistent environment across different development machines and deployment targets, reducing the "it works on my machine" problem.

- Docker containers provide isolation for the CLI tool, preventing it from interfering with the host system or other applications.

- Docker enables reproducibility via defining the entire environment, including dependencies and configurations, using a Dockerfile. 

### Tools available in the market
We just need [Docker](https://www.docker.com/) installed and created relevant `Dockerfile` and `docker-compose.yaml`

## Localization

### Introduction
The process of adapting a product, service, or content to meet the linguistic, cultural, and functional requirements of a specific locale or target audience.

### Why it matters
- Localization can help increase the tool's adoption and usability in diverse environments

- Localization makes CLI tools accessible to a broader audience by providing support for multiple languages.

- Different regions have varying measurement units. Localizing a CLI tool ensures that measurement units align with the conventions and expectations of users in specific regions.

### Tools available in the market
- Python's [`gettext`](https://docs.python.org/3/library/gettext.html) module is a popular choice for localization and internationalizing Python programs.

- [`Babel`](https://babel.pocoo.org/en/latest/intro.html) is a comprehensive library that supports localization and internationalizing in Python
