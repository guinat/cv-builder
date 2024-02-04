from flask import flash


def info(message):
    flash(message, 'info')


def success(message):
    flash(message, 'success')


def warning(message):
    flash(message, 'warning')


def danger(message):
    flash(message, 'danger')
