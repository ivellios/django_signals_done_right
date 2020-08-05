# Signals done right - the demo

This is a demo project, showing how to use [Django Signals](https://docs.djangoproject.com/en/3.1/topics/signals/) properly.

New django users tend to use signals as they are mainly shown in the documentation and other tutorials. 
They create receivers for `pre_save` and `post_save` signals hiding implementation, turning the apps hard to
read and debug in the future. 

While `pre_save` and `post_save` signals on models can be very useful for utility apps that may watch signals like this,
they should not be used for implementing business functionality depending on the models from the other app.

Instead the depending app should expose in its API by adding proper custom signals driven from the business logic. 
Such signals can then be handled by receivers in other apps (dependants). This way developers can keep control
on the signals and data flow in their apps. 

# Example

In this repository I have created simple example of a project with `orders` app and dependant app `invoices`, which 
is supposed to catch actions in the system and send invoices (simplified version just prints text on console).  

It shows usage of signals with two patterns. First of them is the bad one depending on using `post_save` signal.
The second one uses signals exposed and dispatched by `orders` app: `order_is_processed` and `order_sent`.

# How to use?

The best option is to create your own virtual env. Then install requiremeents and run:

```bash
$ python manage.py shell_plus
```

In the shell CLI create order object and run actions on it to see signals in action. 

```python
o = Order.objects.create(quantity=5, cost=5.00)
o.process() # will set status to processed
o.send() # will set status to sent
```

# Why does it matter?

Over time, when developer returns to the orders app code, they may not remember, that some dependant app was 
watching the `post_save` signals and it is easy to mess up with the `invoice` app without even noticing.

Explicit use of custom signals tells developers that some other actions can be taken in the code. It is also
easier to find them as they are explicitly named and over time (and dozens of added apps) they won't get lost 
in the spaghetti of all `post_save` signals in the project codebase. 
