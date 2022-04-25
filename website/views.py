from flask import Blueprint, redirect, render_template, request, flash, send_file, url_for, session
from .models import Question
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    create_questions_list()
    if Question.query.count() == 0:
        return render_template("base.html")

    session["current_question"] = 1
    session["questions_correct"] = 0

    return redirect(url_for("views.question", question_id=session["current_question"]))

@views.route("/<int:question_id>", methods=["GET", "POST"])
def question(question_id):
    question = Question.query.get_or_404(question_id)
    if request.method == "POST":

        if request.form["answer"] == question.answer:
            session["questions_correct"] = session["questions_correct"] + 1
            flash("Vous avez la bonne réponse!", category="success")
        else:
            flash(f"Vous n'avez pas trouvé la bonne réponse! La bonne réponse était {question.answer}!", category="error")

        if question_id < Question.query.count():
            session["current_question"] = question_id + 1
            return redirect(url_for("views.question", question_id=session["current_question"]))

        return redirect(url_for("views.complete"))

    return render_template("question.html", question=question)

@views.route("/complete")
def complete():
    questions_correct = session["questions_correct"]
    total = Question.query.count()
    return render_template("complete.html", correct=questions_correct, total=total)

def create_questions_list():
    db.session.query(Question).delete()
    questions = [
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908704878!6m8!1m7!1sCAoSLEFGMVFpcE83ZkpHOVBhLVNvNUNOSHBtR2tnTHA4ZG9QNk1WVTdKSjJPSFpX!2m2!1d33.88871985!2d35.47022938!3f7.21!4f6.409999999999997!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908793698!6m8!1m7!1sCAoSLEFGMVFpcE9DYjdfaGI0R01zSWNzMUI3Vk5zQ19OQ05CVkE2TnN1UlIybVR6!2m2!1d48.8613085721185!2d2.335389330983162!3f156.13!4f8.340000000000003!5f0.7820865974627469",
            answer="france"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650907861878!6m8!1m7!1soUBW2OPfg2xx7Mahh5B7oQ!2m2!1d34.11852823671052!2d35.64530421955928!3f203.1064343903531!4f-7.772004365928666!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650907677024!6m8!1m7!1sCAoSLEFGMVFpcE41Wk1Nbk01YjlYQ29VNlhQYXFtbkp4YjZoU0pEaDR4c0M1NG4t!2m2!1d48.85335329999999!2d2.3489!3f357.02872944032424!4f21.292272755553256!5f0.8160813932612223",
            answer="france"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908180401!6m8!1m7!1sCAoSLEFGMVFpcE5FUXVvZTVRUngyaGdpamh6RjZwT3A2SWNkM2pSNFJFeTdHLTNH!2m2!1d44.87818217712076!2d-0.5288085226136445!3f234.59!4f7.569999999999993!5f0.7820865974627469",
            answer="france"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908311270!6m8!1m7!1sCAoSLEFGMVFpcE1rRjBsOXpLNER5SVROR1lCb1RjcEtQdml6ZWlQTkRkR3ZaRDhp!2m2!1d34.0060746!2d36.2040086!3f208.10643908703108!4f25.44003329114676!5f0.4000000000000002",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908355997!6m8!1m7!1sCAoSLEFGMVFpcE1UNHl4MlUxazZJamIwVUNYcHIzNmxfc0tqOUE4cVhyOTZDckVl!2m2!1d42.8396515!2d2.9181792!3f276.54946629858983!4f12.231256889701413!5f0.7820865974627469",
            answer="france"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908475587!6m8!1m7!1sCAoSLEFGMVFpcE9QNHJkYXZjWFVPRXRFLUlrbXBac2V5RDdIdHFkeXJ5UklILVhm!2m2!1d34.30417738994621!2d35.86752889896871!3f129.29!4f1.980000000000004!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908392027!6m8!1m7!1sCAoSLEFGMVFpcE9BRW5zUEpvNWU3aTJDRVBQWlU3UHZrVFp5QTJFVDY5REVsd09U!2m2!1d48.581363549981!2d7.751126049989807!3f315.87!4f27.17!5f0.7820865974627469",
            answer="france"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908530136!6m8!1m7!1sCAoSLEFGMVFpcE9jMmRob2syQU1XYUR4ZHpGWmxuM0xqMFdJeW5VbnN4ZFJ4eEtw!2m2!1d34.20586467!2d35.83976538!3f0!4f0!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908633844!6m8!1m7!1sCAoSLEFGMVFpcE4wdlhpQlE0MHJwMmFQbFN2ZUY3OUt4OHpodG13OWdNc1RRSjdr!2m2!1d34.283036!2d35.946453!3f42.97!4f20.03!5f0.8160813932612223",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908860719!6m8!1m7!1sCAoSLEFGMVFpcE13Qkw5cEM0X0tqNGFjbWVLdjRxWDZERkVsZXpGbWJkbDAzck5z!2m2!1d48.84475764603103!2d2.234607975240124!3f96.82!4f20.870000000000005!5f0.7820865974627469",
            answer="france"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908912212!6m8!1m7!1s0I9uPbpwBLkK1PC4uUuIRw!2m2!1d43.09841654095399!2d3.108143660294814!3f269.26!4f-6.359999999999999!5f0.7820865974627469",
            answer="france"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909145054!6m8!1m7!1sCAoSLEFGMVFpcE9fM3kyX05BMk1yc192SFdOVm82U3dpbkRVdVEwM2Q0OXh2YTJs!2m2!1d33.8961973!2d35.5048573!3f22.13!4f6.769999999999996!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650908971663!6m8!1m7!1sgbAACtURFQQP-tAcd6NuQQ!2m2!1d33.89918440553348!2d35.47938581390265!3f326.43!4f3.280000000000001!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909027716!6m8!1m7!1s1GCPySw4Ekg-uIsu-NnBRQ!2m2!1d33.89994465547682!2d35.47928156514755!3f199.75!4f14.700000000000003!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909098170!6m8!1m7!1sCAoSLEFGMVFpcE81Zk5rc0cwZ0JJcVM1TUFYenFua0JSX2hFekF5Qk8waGZDSXN0!2m2!1d33.89596928251569!2d35.50482810018455!3f307.66!4f7.989999999999995!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909226242!6m8!1m7!1sCAoSLEFGMVFpcE9mWThGUjMtb3ZaWkFLTFZtd1BoN3hzOXRxU2kxV2ZlMWFmS3lY!2m2!1d33.8965509!2d35.5047007!3f166.24!4f24.480000000000004!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909269408!6m8!1m7!1sCAoSLEFGMVFpcFBFby1FZ3hGOXZ1Ukh1aUhXTEdBcTRfLUVfUUkxY3JiSC1qdUs5!2m2!1d33.896394938851!2d35.50509578412!3f319.78!4f4.180000000000007!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909321086!6m8!1m7!1sR-7hnqJjQaNvKOeSvz3yjA!2m2!1d33.8969961855402!2d35.50245343121829!3f23.21!4f7.760000000000005!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909354785!6m8!1m7!1sBuRBlmZg30jfhBaDDAPjRw!2m2!1d33.89618559757055!2d35.50232054711371!3f70.35!4f9.159999999999997!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909410740!6m8!1m7!1sCAoSLEFGMVFpcE9Yc3VTMENxQlg5TlBpYXc3MkVEU0hjMzFmNTdLUWtBMzMzU3V2!2m2!1d33.89922235175111!2d35.50349592507769!3f267.09!4f26.269999999999996!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909472159!6m8!1m7!1sCAoSLEFGMVFpcE1wZHpfVk8zU1pJNEk1ZjZKekZwZ21jcHVycVVjS21yamVrbU9q!2m2!1d33.89905944148631!2d35.50494449000715!3f277.48189976997514!4f21.093401028258356!5f0.7820865974627469",
            answer="liban"),
        Question(
            source="https://www.google.com/maps/embed?pb=!4v1650909515438!6m8!1m7!1sCAoSLEFGMVFpcE9vZHZRR2EtLWQ2djZiU3E5SHVma3RNNDlaT3lJSTcwSDNjSHVP!2m2!1d33.89877225311304!2d35.50310731831451!3f326.26!4f6.319999999999993!5f0.4000000000000002",
            answer="liban"),
    ]
    db.session.add_all(questions)
    db.session.commit()