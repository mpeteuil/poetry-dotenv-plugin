#!/usr/bin/env bash

function create_dotenv_file() {
  # Setup .env file so the plugin can do its job
  echo "export MY_ENV_VAR='foo'" > .env
}

function delete_dotenv_file() {
  # Tear down .env file since we no longer need it
  rm -f .env
}

function test_end_to_end_system_with_default_dotenv_file() {
  # Setup
  local expected
  expected='foo'
  create_dotenv_file

  local output
  output=$(poetry run python -c "import os; print(os.environ['MY_ENV_VAR'])")

  # Cleanup
  delete_dotenv_file

  if [ "$expected" = "$output" ]; then
    printf "test_end_to_end_system_with_default_dotenv_file: PASSED\n"
  else
    printf "Expected '$expected', but got '%s'.\n" "$output"
    exit 1
  fi
}

function test_end_to_end_system_with_dotenv_location_override() {
  # Setup
  local expected
  expected='bar'
  local new_dotenv_path
  new_dotenv_path="$PWD/tests/tmp"
  create_dotenv_file

  # Override the file that was just created
  mkdir -p "$new_dotenv_path" && echo "export MY_ENV_VAR='bar'" > "$new_dotenv_path/.env"

  local output
  output=$(export POETRY_DOTENV_LOCATION="$new_dotenv_path/.env" && poetry run python -c "import os; print(os.environ['MY_ENV_VAR'])")

  # Cleanup
  rm -rf "$new_dotenv_path"
  delete_dotenv_file

  if [ "$expected" = "$output" ]; then
    printf "test_end_to_end_system_with_dotenv_location_override: PASSED\n"
  else
    printf "Expected '$expected', but got '%s'.\n" "$output"
    exit 1
  fi
}

function test_end_to_end_system_with_default_env_overrides() {
  # Setup
  local expected
  expected='foo'
  create_dotenv_file

  local output
  output=$(export MY_ENV_VAR='bar' && poetry run python -c "import os; print(os.environ['MY_ENV_VAR'])")

  # Cleanup
  delete_dotenv_file

  if [ "$expected" = "$output" ]; then
    printf "test_end_to_end_system_with_default_env_overrides: PASSED\n"
  else
    printf "Expected '$expected', but got '%s'.\n" "$output"
    exit 1
  fi
}

function test_end_to_end_system_without_env_overrides() {
  # Setup
  local expected
  expected='bar'
  create_dotenv_file

  local output
  output=$(export MY_ENV_VAR='bar' POETRY_DOTENV_DONT_OVERRIDE=true && poetry run python -c "import os; print(os.environ['MY_ENV_VAR'])")

  # Cleanup
  delete_dotenv_file

  if [ "$expected" = "$output" ]; then
    printf "test_end_to_end_system_without_env_overrides: PASSED\n"
  else
    printf "Expected '$expected', but got '%s'.\n" "$output"
    exit 1
  fi
}

function test_end_to_end_system_without_loading_dotenv_file() {
  # Setup
  local expected
  expected='Nonexistent Variable'
  create_dotenv_file

  local output
  output=$(export POETRY_DONT_LOAD_ENV=true && poetry run python -c "import os; print(os.environ.get('MY_ENV_VAR', '$expected'))")

  # Cleanup
  delete_dotenv_file

  if [ "$expected" = "$output" ]; then
    printf "test_end_to_end_system_without_loading_dotenv_file: PASSED\n"
  else
    printf "Expected '$expected', but got '%s'.\n" "$output"
    exit 1
  fi
}

test_end_to_end_system_with_default_dotenv_file
test_end_to_end_system_with_dotenv_location_override
test_end_to_end_system_with_default_env_overrides
test_end_to_end_system_without_env_overrides
test_end_to_end_system_without_loading_dotenv_file
