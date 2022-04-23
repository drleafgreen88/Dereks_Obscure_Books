from flask import Flask, redirect, render_template, Blueprint, request

book_store_bp = Blueprint('book_store', __name__)