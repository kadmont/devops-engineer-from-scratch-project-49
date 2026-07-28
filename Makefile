.PHONY: install brain-games build package-install lint test setup

install:
	uv sync

add-promt:
	uv add prompt

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

test:
	uv run pytest
	
setup: install
	@echo "Setup complete!"

brain-games:
	uv run brain-games