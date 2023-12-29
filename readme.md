#!/bin/bash


ERRORS=0

function check_errors {
  if [ $1 -ne 0 ]; then
    echo "Ошибка: $2"
    ERRORS=$((ERRORS + 1))
  fi
}


prettier --check "src/**/*.js" "src/**/*.ts"
check_errors $? "Prettier обнаружил ошибки форматирования"


if [ $ERRORS -ne 0 ]; then
  echo "Прошло успешно с ошибками. Отмена коммита."
  exit 1
else
  echo "Pre-commit проверка успешно завершена."
fi

exit 0

