========
Examples
========

Running sequential tasks
========================

This is the simplest workflow one can think of, it simply consists in running process A and using its output to feed process B. To make the examples more concrete, let's imagine a ``random_word`` process that takes as input ``n`` the number of random words to return, and returns ``text``, a string joining all these words separated by a space. Our second process ``count_characters`` will return ``n`` the number of a given character (a, b, c) in input ``text``. A workflow to generate 10 random words and count the number of *e* would then look like this:

.. code-block:: json

   {
        "name" : "count_e",
        "tasks": [
            {
                "name": "create_sentence",
                "url": "http://myserver.org:8090/wps",
                "identifier": "random_word",
                "inputs": {
                    "n": 10,
                    }

            },
            {
                "name": "count_letter_e",
                "url": "http://myserver.org:8090/wps",
                "identifier": "count_characters"
                "linked_inputs": {
                    "text": {
                        "task": "create_sentence",
                        "output": "text",
                        }
                    },
                "inputs": {
                    "char": "e"
                    }
            },
         ]
   }

When the ``count_e`` workflow is launched, the first task is executed using ``n=10``. Then the second task is executed using ``char=e``, and the ``text`` value taken from the ``text`` output of the ``create_sentence`` task, defined in ``linked_inputs`` by an :json:object:`Input_description` object.