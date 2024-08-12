.PHONY: help
.DEFAULT_GOAL := help
export AWS_PAGER :=

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init: ## bootstrap the environment
	cdk bootstrap

plan: ## show the changes (diff)
	cdk diff

apply: ## apply the changes
	cdk deploy

synth: ## synth the changes
	cdk synth

output: ## show the output
	aws cloudformation describe-stacks --stack-name DataSourcesStack --query 'Stacks[0].Outputs'
