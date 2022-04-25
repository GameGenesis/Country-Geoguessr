from flask import Blueprint, redirect, render_template, request, flash, send_file, url_for, session
from .models import Question
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    create_questions_list()
    if Question.query.count() == 0:
        return render_template("base.html")

    session["current_question"] = 0
    session["questions_correct"] = 0

    return redirect(url_for("views.question", question_id=0))

@views.route("/<int:question_id>", methods=["GET", "POST"])
def question(question_id):
    question = Question.query.get_or_404(question_id)
    if request.method == "POST":

        if request.form["answer"] == question.answer:
            session["questions_correct"] = session["questions_correct"] + 1
            flash("Vous avez la bonne réponse!", category="success")
        else:
            flash(f"Vous n'avez pas trouvé la bonne réponse! La bonne réponse était {question.answer}", category="error")

        session["current_question"] = question_id + 1
        return redirect(url_for("views.question", question_id=session["current_question"]))

    return render_template("question.html", question=question)

def create_questions_list():
    questions = [
        Question(
            id = 0,
            source="https://www.google.com/maps/embed?pb=!4v1650138478545!6m8!1m7!1sCAoSLEFGMVFpcE8yQ2VBZ2Z5WFBRd0toNWVYZndRZTg2UElFVXhuNDdDS3kyWERF!2m2!1d33.92678194344445!2d35.80716769736532!3f166.6389652726608!4f4.771130284143823!5f0.7820865974627469",
            answer="liban"),
        Question(
            id = 1,
            source="https://www.google.com/maps/embed?pb=!4v1650907677024!6m8!1m7!1sCAoSLEFGMVFpcE41Wk1Nbk01YjlYQ29VNlhQYXFtbkp4YjZoU0pEaDR4c0M1NG4t!2m2!1d48.85335329999999!2d2.3489!3f357.02872944032424!4f21.292272755553256!5f0.8160813932612223",
            answer="france")
    ]
    db.session.add_all(questions)
    db.session.commit()