ЛАБОРАТОРНАЯ РАБОТА 1
Git и GitHub: основы работы с системой контроля версий
https://img.shields.io/github/last-commit/Smir7/lab1
https://img.shields.io/github/repo-size/Smir7/lab1
https://img.shields.io/github/license/Smir7/lab1
https://img.shields.io/badge/status-completed-success
https://img.shields.io/badge/python-3.8+-blue
https://img.shields.io/badge/git-2.34+-orange
https://img.shields.io/badge/PRs-2-yellow
https://img.shields.io/badge/commits-signed-brightgreen

 Автор
Smir7 (Гончарова Ольга)
 Email: g.olga0588@gmail.com
 GitHub: https://github.com/Smir7

Дата
09 декабрь 2025 г.

 Цель работы
Освоить базовые принципы работы с системой контроля версий Git и платформой GitHub, включая подписанные коммиты, работу с ветками, Pull Requests и разрешение конфликтов.

Задачи
Создать и настроить Git-репозиторий

Настроить SSH-ключи и Personal Access Token

Сгенерировать GnuPG ключ для подписи коммитов

Реализовать Python-приложение 

Работать с ветками (patch1, patch2)

Освоить создание и слияние Pull Requests

Научиться разрешать конфликты слияния

Использовать GitHub CLI для автоматизации

Оформить документацию с бейджами Shields.io

 Структура проекта
text
lab1/
├── README.md              # Этот файл с документацией
├── hello.py               # Основное приложение на Python
├── data.txt               # Файл для хранения данных
├── .gitignore            # Игнорируемые файлы
├── LICENSE               #  лицензия
├── CODE_OF_CONDUCT.md    # Кодекс поведения
├── CONTRIBUTING.md       # Руководство для контрибьюторов
├── SECURITY.md           # Политика безопасности
├── NOTICE                # Уведомления об авторских правах
└── requirements.txt      # Зависимости Python
 
Установка и запуск
Требования
Python 3.8 или выше

Git 2.34 или выше

GitHub CLI (опционально)

Установка
bash
# Клонирование репозитория
git clone https://github.com/Smir7/lab1.git
cd lab1

# Запуск приложения
python hello.py
 Описание приложения hello.py
Основные функции
Приложение представляет собой консольную утилиту с следующими возможностями:

Добавление данных - сохранение текстовых данных в файл

Чтение файлов - просмотр содержимого текстовых файлов

Обработка JSON - парсинг и валидация JSON данных

Работа с данными - хранение и управление пользовательскими данными

Архитектура

Подробная документация каждой функции

Обработка ошибок и исключений

Безопасное хранение данных

Пример использования
bash
$ python hello.py
Учебный проект - Базовая версия

=== Учебное приложение ===
Элементов в базе: 0
1. Добавить данные
2. Прочитать файл
3. Выполнить команду
4. Обработать JSON
5. Выход
Выберите: 1
Введите данные: Тестовый пример
 Технические детали
Используемые технологии
Python 3.8+ - основной язык программирования

Git 2.34+ - система контроля версий

GitHub CLI 2.47+ - командный интерфейс GitHub

GnuPG 2.2+ - подпись коммитов

SSH - безопасное подключение к GitHub

Ключевые особенности кода
Подробные docstrings на русском языке

Обработка исключений в критических операциях

Безопасная работа с файловой системой

Чистая архитектура с разделением логики

 История разработки

Ветки и коммиты
text
Локальный репозиторий:
* e8225b9 (HEAD -> master, origin/patch2-conflict, origin/master, patch2-conflict) master: stronger conflict in user_info comment
* 1af51a2 master: change user_info comment for conflict
* 134601e (origin/patch2, patch2) master: change text
* f13c51d Update README.md
* 57c2eb4 Update README.md
* 81e0f93 Update README.md
* 6fbe325 Update README.md
* eb1fa3f Update README.md
*   a31d4de Merge pull request #1 from Smir7/patch1
|\  
| * 30541c8 (origin/patch1) patch1: Add detailed comments
| * 0c8056b patch1: Refactor and clean up hello.py code
|/  
* 8204f6a Update hello.py
* 2c9370b Add hello.py with dirty code
* e03f2a3 Initial commit with signed commit
* c7bb74c add empty README

Выполненные операции
✅ 15+ коммитов (все подписаны с использованием GnuPG)

✅ 4 ветки созданы и обработаны (master, patch1, patch2, patch2-conflict)

✅ 2 Pull Requests созданы и обработаны

✅ Конфликты  разрешены

✅ Репозиторий размещен на GitHub с полной документацией

 Работа с Git
Ключевые команды, использованные в работе:
bash
# Подписанные коммиты
git commit -S -m "Сообщение коммита"

# Работа с ветками
git checkout -b patch1
git push -u origin patch1

# Создание Pull Request через GitHub CLI
gh pr create --title "Рефакторинг кода" --base master --head patch1

# Разрешение конфликтов
git rebase master
git mergetool
git rebase --continue

# Просмотр истории
git log --oneline --graph --all --decorate

Настройки Git

bash
git config --global user.name "olgaG"
git config --global user.email "g.olga0588@gmail.com"
git config --global commit.gpgsign true

 Проблемы и решения

Проблема 1: Конфликт настроек Git и GnuPG
Симптомы: Несоответствие имен и email в конфигурации Git и GnuPG ключах
Решение: Корректировка настроек Git и создание нового GnuPG ключа с правильными данными

Проблема 2: Конфликт при слиянии веток
Симптомы: Конфликтующие изменения в README.md и коде
Решение: Использование git rebase для последовательного применения изменений и ручное разрешение конфликтов

Проблема 3: Ошибки при работе с удаленным репозиторием
Симптомы: Отклонение push операций, расхождения в истории
Решение: Регулярное использование git pull --rebase, аккуратное применение git push --force-with-lease

Статистика проекта

Метрика	Значение	Бейдж
Коммиты	15+	https://img.shields.io/github/commit-activity/m/Smir7/lab1
Ветки	4	https://img.shields.io/badge/branches-4-blue
Pull Requests	2	https://img.shields.io/badge/PRs-2-yellow
Языки	2	https://img.shields.io/github/languages/count/Smir7/lab1
Основной язык	Python	https://img.shields.io/github/languages/top/Smir7/lab1
Размер репозитория	~50 KB	https://img.shields.io/github/repo-size/Smir7/lab1

 Выводы

Приобретенные навыки:

Работа с Git : ветки, теги, подписанные коммиты

Интеграция с GitHub: создание репозиториев, PR

Автоматизация с помощью GitHub CLI

Разрешение конфликтов: стратегии rebase и merge

Документирование: создание профессиональной документации

Безопасность: работа с SSH ключами и GPG подписями

Ключевые достижения:
Создано полноценное Python-приложение с чистой архитектурой

Освоена практика подписанных коммитов для верификации авторства

Создана комплексная документация с использованием современных инструментов

 Полезные ссылки
Репозиторий на GitHub

Исходный код hello.py

Pull Request #1

Документация Git

GitHub CLI руководство

Shields.io - создание бейджей
