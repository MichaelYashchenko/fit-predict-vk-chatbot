.DEFAULT_GOAL = bot
.PHONY: help bot

define find.functions
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done
endef

help: # Show help for each of the Makefile recipes.
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

# Components
# Components
bot: # Run vk chatbot.
	python3 -m src.main