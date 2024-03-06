from flask import Blueprint, flash, redirect, render_template, request
from reviews_project.models import MovieReview, db 
from reviews_project.forms import MovieReviewForm  
from reviews_project.helpers import get_movie_details

site = Blueprint('site', __name__, template_folder='site_templates')



@site.route('/')
def home():
    all_reviews = MovieReview.query.all()
    reviews_with_details = []

    for review in all_reviews:
        movie_details = get_movie_details(review.movie_title)
        if movie_details != "Movie not found.":
            review_data = {
                'review': review,
                'movie_details': movie_details
            }
            reviews_with_details.append(review_data)
        else:
            reviews_with_details.append({'review': review})

    return render_template('front.html', reviews=reviews_with_details)



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

@site.route('/update/<review_id>', methods=['GET', 'POST'])
def update_review(review_id):
    review = MovieReview.query.get_or_404(review_id)
    form = MovieReviewForm(obj=review)
    if form.validate_on_submit():
        review.movie_title = form.movie_title.data
        review.review_text = form.review_text.data
        review.rating = float(form.rating.data)
        review.reviewer_name = form.reviewer_name.data
        db.session.commit()
        flash('Review updated successfully!', 'success')
        return redirect('/')
    return render_template('update_review.html', form=form, movie_review=review)

@site.route('/delete/<review_id>')
def delete_review(review_id):
    review = MovieReview.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    flash('Review deleted successfully!', 'success')
    return redirect('/')
