from flask import Blueprint, redirect, render_template, request, flash, send_file, url_for, session
from .models import Question
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    if Question.query.count() == 0:
        return render_template("base.html")

    session["current_question"] = 0
    session["questions_correct"] = 0

    return redirect(url_for("views.question", question_id=0))

@views.route("/<int:question_id>", methods=["GET", "POST"])
def question(question_id):
    if request.method == "POST":
        question = Question.query.get_or_404(question_id)

        if request.form["answer"] == question.answer:
            session["questions_correct"] = session["questions_correct"] + 1

        session["current_question"] = question_id + 1
        return redirect(url_for("views.quiz", question_id=session["current_question"]))

    return render_template("question.html", question=question)