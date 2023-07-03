# terminal-todo
A terminal-based todo table that allows you to write .csv files and print them as ASCII tables.

There is no love in my heart for paper planners, and I need another webapp to frequent like I need a hole in the head. To brush up on my Python, I created a utility to create ASCII tables in the terminal, and bashed together a quick controller script to let me read & write to a list of tables in a simple CLI. For usage, todo help or see below:

<pre>
+help----------------------------------+--------------------------------------+
| command                              | effect                               |
+--------------------------------------+--------------------------------------+
| help                                 | shows this page                      |
+--------------------------------------+--------------------------------------+
| write <name>                         | edits or creates a table in the dat- |
|                                      | a directory                          |
+--------------------------------------+--------------------------------------+
| <name>                               | displays table                       |
+--------------------------------------+--------------------------------------+
| remove <name>                        | permanently deletes a table          |
+--------------------------------------+--------------------------------------+
</pre>
