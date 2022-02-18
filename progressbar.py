from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def data_page():
    
    if request.method == 'POST':
        # formDict = request.form.to_dict()
        filesDict = request.files.to_dict()
        # print('Forms:::', formDict)
        # print('files:::', filesDict)
        uploadData=request.files['media']
        data_file_name = uploadData.filename
        # print('data_file_name:::', data_file_name)
        # print(os.path.join(app.root_path,data_file_name))
        uploadData.save(os.path.join(app.root_path,'uploads\\'+data_file_name))

    return render_template("upload.html")

if __name__=='__main__':
    app.run(debug=True)