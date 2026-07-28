.PHONY: install brain-games build package-install lint test setup

install:
	uv sync

build:
	uv build

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check

test:
	uv run pytest