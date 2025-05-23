from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []  #seznam úkolů

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)  #homepage

@app.route("/ukoly", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        #formulář
        tasks.append({
            "id": len(tasks),
            "title": request.form["nazev"],
            "description": request.form["popis"],
            "start": request.form["start_date"],
            "end": request.form["end_date"],
            "done": False
        })
        return redirect("/") 
    return render_template("ukoly.html")  #zorbazení formuláře

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True  #označení úkolu jako hotový
    return redirect("/")

@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    if 0 <= task_id < len(tasks):
        #Úprava úkolu
        tasks[task_id]["title"] = request.form["nazev"]
        tasks[task_id]["description"] = request.form["popis"]
        tasks[task_id]["start"] = request.form["start_date"]
        tasks[task_id]["end"] = request.form["end_date"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
