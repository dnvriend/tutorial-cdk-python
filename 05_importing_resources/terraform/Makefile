.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init: ## init terraform
	terraform init -upgrade

plan: init ## plan terraform and create plan file
	terraform plan -out=terraform.plan

diff: plan ## show the changes (diff)
	terraform show -no-color terraform.plan | egrep -E '(Plan:|Changes)' || echo "No changes detected"

apply: ## apply terraform based on the plan file
	terraform apply -auto-approve terraform.plan
