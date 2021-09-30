

try:
    from flask import Flask, render_template,request,redirect,flash,url_for,json
    import youtube_dl
    from random import random
#     from flask_sqlalchemy import SQLAlchemy
#     from sqlalchemy.sql import func
#     import sentry_sdk
#     import netrc
#     from sentry_sdk.integrations.flask import FlaskIntegration
except Exception as e:
    print(e)
# netrc = netrc.netrc()

app = Flask(__name__)
app.secret_key='iamsecret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://iwritee_sandboxuser:0w16oxSsQ$C1@23.229.0.146/iwritee_sandboxdb'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/blogs'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
# db = SQLAlchemy(app)

# class SeoBlogs(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id = db.Column(db.Integer, primary_key=True)
#     title=db.Column(db.String(191),unique=True)
#     meta_title=db.Column(db.String(191))
#     meta_description=db.Column(db.String(80))
#     blog_url=db.Column(db.String(191))
#     author=db.Column(db.String(100))
#     main_img=db.Column(db.String(191))
#     image_alt=db.Column(db.String(191))
#     image_title=db.Column(db.String(191))
#     website=db.Column(db.String(80))
#     author_id=db.Column(db.Integer)
#     created_by = db.Column(db.Integer)
#     last_update_by = db.Column(db.Integer)
#     created_date=db.Column(db.DateTime(timezone=True), server_default=func.now())
#     last_update_date=db.Column(db.DateTime(timezone=True), server_default=func.now())
#     is_draft=db.Column(db.Integer)
#     category_id=db.Column(db.Integer,db.ForeignKey('seo_blog_categories.id'),nullable=False)
#     sub_category_id = db.Column(db.Integer, db.ForeignKey('seo_blog_sub_categories.id'), nullable=False)
#     seo_blog_detail=db.relationship('SeoBlogsDetail',backref='seo_blogs',lazy=True)

# class SeoBlogsDetail(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     blog_detail=db.Column(db.String(230))
#     blog_id=db.Column(db.Integer,db.ForeignKey('seo_blogs.id'),nullable=False)

# class SeoBlogsAuthors(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(80))
#     gender=db.Column(db.String(80))
#     bio=db.Column(db.String(230))
#     website=db.Column(db.String(80))
#     added_by=db.Column(db.Integer)
#     updated_at=db.Column(db.DateTime(timezone=True), server_default=func.now())
#     created_at=db.Column(db.DateTime(timezone=True), server_default=func.now())

# class SeoBlogCategories(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     category_name = db.Column(db.String(80))
#     category_name_slug =db.Column(db.String(80))
#     seo_blogs = db.relationship('SeoBlogs', backref='seo_blog_categories', lazy=True)
#     seo_blog_sub_categories=db.relationship('SeoBlogSubCategories',backref='seo_blog_categories',lazy=True)

# class SeoBlogSubCategories(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     sub_category_name=db.Column(db.String(80))
#     sub_category_slug=db.Column(db.String(80))
#     seo_blogs = db.relationship('SeoBlogs', backref='seo_blog_sub_categories', lazy=True)
#     category_id=db.Column(db.Integer,db.ForeignKey('seo_blog_categories.id'),nullable=False)



@app.route('/')
def home():
#     stmt = db.session.query(SeoBlogs, SeoBlogsDetail, SeoBlogSubCategories).filter(
#         SeoBlogsDetail.blog_id == SeoBlogs.id and SeoBlogs.sub_category_id == SeoBlogSubCategories.id).group_by(
#         SeoBlogs.id).order_by(SeoBlogs.id).order_by(SeoBlogsDetail.id).order_by(func.random()).limit(3).all()
    return render_template('index.html')

# @app.route('/format' ,methods=['POST'])
# def from_format():
# #     stmt = db.session.query(SeoBlogs, SeoBlogsDetail, SeoBlogSubCategories).filter(
# #         SeoBlogsDetail.blog_id == SeoBlogs.id and SeoBlogs.sub_category_id == SeoBlogSubCategories.id).group_by(
# #         SeoBlogs.id).order_by(SeoBlogs.id).order_by(SeoBlogsDetail.id).order_by(func.random()).limit(3).all()

#     fburl = request.form['url']
#     if 'https://m.youtube.com/watch?' in fburl:
#                 flash('Not a Valid Fb UrL')
#                 return redirect(url_for('home'))
#     elif 'https://youtu.be/' in fburl:
#         flash('Not a Valid Fb UrL')
#         return redirect(url_for('home'))
#     elif 'https://www.youtube.com/watch?' in fburl:
#         flash('Not a Valid Fb UrL')
#         return redirect(url_for('home'))
#     try:
#         with youtube_dl.YoutubeDL() as ytdl:
#             url=ytdl.extract_info(fburl ,download=False,netrc=netrc)
#             vidFormat =url['formats']
#             vidTital=url['title']


#         return render_template('converter.html', vidFormat=vidFormat, iframe=url, fburl=fburl,vidTital=vidTital,)
#     except Exception as e:
#         print(e)
#         flash("Not a valid facebook video URL")
#         flash("Paste a valid facebook video URL")
#         return redirect(url_for('home'))

# @app.route('/download' ,methods=['POST'])
# def vid_download():
#     try:
#         fburl=request.form['fburl']

#         vidindex= int(request.form['vidindex'])
#         with youtube_dl.YoutubeDL() as ytdl:
#             url = ytdl.extract_info(fburl,download=False,netrc=netrc)
#             download_url =(url['formats'][vidindex]['url'])
#         return redirect(download_url+"&dl=1")
#     except Exception as e:
#         print(e)
#         flash('Something went Wrong!')
#         flash('Try again or with another video.')
#         return redirect(url_for('home'))

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contactus.html')

# @app.route('/blog')
# def blog():
#     stmt = db.session.query(SeoBlogs, SeoBlogsDetail, SeoBlogSubCategories).filter(
#         SeoBlogsDetail.blog_id == SeoBlogs.id and SeoBlogs.sub_category_id == SeoBlogSubCategories.id).group_by(
#         SeoBlogs.id).order_by(SeoBlogs.id).order_by(SeoBlogsDetail.id).all()
#     return render_template('blogpage.html',stmt=stmt)
# @app.route('/')
# def blogdetail(blog_id):
#     stmt = db.session.query(SeoBlogs, SeoBlogsDetail).join(SeoBlogs).filter(
#         SeoBlogsDetail.blog_id == blog_id and SeoBlogs.id == SeoBlogsDetail.blog_id).group_by(SeoBlogsDetail.id).all()
#     if stmt:
#         return render_template('blogdetail.html', stmt=stmt)
#     else:
#         return 'ok'
#         # raise HTTPException

@app.route('/term-of-services')
def termofservices():
    return render_template('termOfServices.html')

@app.route('/privacy-policy')
def policy():
    return render_template('privacy-policy.html')

@app.errorhandler(Exception)
def handle_exception(e):
    if e.code ==404:
        return render_template('notfound.html')
    else:
        error_name= e.name
        error_code= e.code
        error_description= e.description
        return render_template('myerror.html',error_name=error_name,error_description=error_description,error_code=error_code)

if __name__ == '__main__':

    app.run(debug=True)
