from flask import Blueprint, flash, redirect, render_template, request
from reviews_project.models import MovieReview, db 
from reviews_project.forms import MovieReviewForm  


site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    # Query your database to grab all movie reviews to display
    all_reviews = MovieReview.query.all()  

    return render_template('front.html', reviews=all_reviews)  


@site.route('/create', methods=['GET', 'POST'])
def create_review():
    form = MovieReviewForm()
    if form.validate_on_submit():
        new_review = MovieReview(
            movie_title=form.movie_title.data,
            review_text=form.review_text.data,
            rating=form.rating.data,
            reviewer_name=form.reviewer_name.data
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect('/')
    
    return render_template('reviewform.html', form=form)

@site.route('/update/<int:review_id>', methods=['GET', 'POST'])
def update_review(review_id):
    review = MovieReview.query.get_or_404(review_id)
    form = MovieReviewForm(obj=review)
    if form.validate_on_submit():
        review.movie_title = form.movie_title.data
        review.review_text = form.review_text.data
        review.rating = form.rating.data
        review.reviewer_name = form.reviewer_name.data
        db.session.commit()
        flash('Review updated successfully!', 'success')
        return redirect('/')
    return render_template('update.html', form=form)

@site.route('/delete/<int:review_id>')
def delete_review(review_id):
    review = MovieReview.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    flash('Review deleted successfully!', 'success')
    return redirect('/')
