
# bot_manager

# config/config.py

class ConfigSettings:
    CONFIG_PATH = "app/cache/bot.json5"
    DEFAULT_CONFIG ='''{
  command_prefix: ".",
  cogs: ["cogs.Main"],
  phrases: {
    start : "Successful starting\\nI logged as {user}\\nStarting during: {during_time}",
    FormatErrorDynConfig : "Ошибка обновления параметра.\\nНе удалось преобразовать {value} в {data_type_need}",
    ConsoleFormatErrorDynConfig: "IncorrectTypeParameter: Failed to update parameter value",
    ConsoleEditInfo: "Параметр {parameter} изменён ---> {convert_value}",
    RunErrorDynConfig: "Parameter \\"%s\\" not set. Func can't start correctly",
    PermErrorDynConfig: "У вас нету прав использовать эту команду",
    ping: "Успешно передано"
  },
  buttons: {
  },
  embeds: {
  },
  modals: {
  },
  cmds: {
    main_cfg: {name: "config", description: "Команда для настройки бота"},
    set_cfg: {name: "set", description: "Изменить настройки бота"},
    del_cfg: {name: "reset", description: "Сбросить настройки/настройку бота"},
    show_cfg: {name: "show", description: "Показать настройки бота"},
    main_ping: {name: "ping", description:  "Проверка ответа от бота"}
  },
  logger: {
    console: { // Set level: 51 for disable console log
      level: "TRACE", //Levels: trace, debug, info, success, warning, error, critical
      format: {
        TRACE: "[grey82][bold]{time:YYYY-MM-DD HH:mm:ss.SSS}\\t| [green]{level: ^8}[/green] | [orange3]{line}[/orange3]:[cyan]{name}[/cyan]:[deep_pink3]{function}()[/deep_pink3] - {message}[/grey82]\\n",
        DEBUG: "[grey82][bold]{time:YYYY-MM-DD HH:mm:ss.SSS}\t| [chartreuse3]{level: ^8}[/chartreuse3] | [orange3]{line}[/orange3]:[cyan]{name}[/cyan]:[deep_pink3]{function}()[/deep_pink3] - {message}[/grey82]\\n",
        INFO: "[grey82][bold]{time:YYYY-MM-DD HH:mm:ss}\\t| [dodger_blue1]{level: ^8}[/dodger_blue1] | ➡️ {message}[/]\\n",
        SUCCESS: "[grey82][bold]{time:YYYY-MM-DD HH:mm:ss}\\t| [chartreuse1]{level: ^8}[/chartreuse1] | ✅  {message}[/]\\n",
        WARNING: "[grey82][bold]{time:YYYY-MM-DD HH:mm:ss}\\t| [yellow2]{level: ^8}[/yellow2] | ⚠️ {message}[/]\\n",
        ERROR: "[grey82][bold]{time:YYYY-MM-DD HH:mm:ss}\\t| [red3]{level: ^8}[/red3] | ❌  [orange3]{line}[/orange3]:[cyan]{name}[/cyan]:[deep_pink3]{function}()[/deep_pink3] - {message}[/]\\n",
        CRITICAL: "[grey82][bold]{time:YYYY-MM-DD HH:mm:ss}\\t| [dark_red]{level: ^8}[/dark_red] | ⛔  {message}[/]\\n"
      }
    },
    file: { // Set level: 51 for disable file log
      level: "INFO", //Levels: trace, debug, info, success, warning, error, critical
      filepath: "./app/cache/logs/bot.log", // Template of log filename
      rotation: "00:00" , // File rotation (default: daily)
      retention: "1 month", // File retention (default: monthly)
      compression: "tar.gz", // Compression format (default: linux archive)
      "encoding": "utf-8", // file encoding
      format: {
        TRACE: "{time:YYYY-MM-DD HH:mm:ss.SSS}\\t| {level: ^8} | {name}:{function}:{line} - {message}\\n",
        DEBUG: "{time:YYYY-MM-DD HH:mm:ss.SSS}\\t| {level: ^8} | {name}:{function}:{line} - {message}\\n",
        INFO: "{time:YYYY-MM-DD HH:mm:ss}\\t| {level: ^8} | {message}\\n",
        SUCCESS: "{time:YYYY-MM-DD HH:mm:ss}\\t| {level: ^8} | {message}\\n",
        WARNING: "{time:YYYY-MM-DD HH:mm:ss}\\t| {level: ^8} | {message}\\n",
        ERROR: "{time:YYYY-MM-DD HH:mm:ss}\\t| {level: ^8} | {message}\\n",
        CRITICAL: "{time:YYYY-MM-DD HH:mm:ss}\\t| {level: ^8} | {message}\\n"
      }
    }
  }
}'''
