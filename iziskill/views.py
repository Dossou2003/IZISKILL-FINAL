from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import *

#  about par DOHA Primael

def about(request):
    return render(request, 'about.html')

def about_dark(request):
    return render(request, 'about-dark.html')


# blog DOHA Primael 
def blog(request):
    return render(request, 'blog.html')
def blog_dark(request):
    return render(request, 'blog-dark.html')
def blog_details(request):
    return render(request, 'blog-details.html')
def blog_details_dark(request):
    return render(request, 'blog-details-dark.html')



# contact par DOHA Primael 
def contact(request):
    return render(request, 'contact.html')
def contact_dark(request):
    return render(request, 'contact-dark.html')

# course par DOHA Primael 

def course(request):
    return render(request, 'course.html')
def course_dark(request):
    return render(request, 'course-dark.html')

def courses_details(request):
    return render(request, 'course-details.html')
def courses_details_dark(request):
    return render(request, 'course-details-dark.html')

def courses_details_2(request):
    return render(request, 'course-details-2.html')
def courses_details_3(request):
    return render(request, 'course-details-3.html')

def courses_details_2_dark(request):
    return render(request, 'course-details-2-dark.html')
def courses_details_3_dark(request):
    return render(request, 'course-details-3-dark.html')

def courses_grid(request):
    return render(request, 'course-grid.html')
def courses_grid_dark(request):
    return render(request, 'course-grid-dark.html')
def course_list(request):
    return render(request, 'course-list.html')
def course_list_dark(request):
    return render(request, 'course-list-dark.html')

# error par DOHA Primael 
def error(request):
    return render(request, 'error.html')
def error_dark(request):
    return render(request, 'error-dark.html')

# event par DOHA Primael
def event_details(request):
    return render(request, 'event-details.html')
def event_details_dark(request):
    return render(request, 'event-details-dark.html')


#home par DOHA Primael
def home_2(request):
    return render(request, 'home-2.html')

def home_2_dark(request):
    return render(request, 'home-2-dark.html')

def home_3(request):
    return render(request, 'home-3.html')

def home_3_dark(request):
    return render(request, 'home-3-dark.html')

def home_4(request):
    return render(request, 'home-4.html')

def home_4_dark(request):
    return render(request, 'home-4-dark.html')

def home_5(request):
    return render(request, 'home-5.html')

def home_5_dark(request):
    return render(request, 'home-5-dark.html')

def home_6(request):
    return render(request, 'home-6.html')

def home_6_dark(request):
    return render(request, 'home-6-dark.html')

def home_7(request):
    return render(request, 'home-7.html')

def home_7_dark(request):
    return render(request, 'home-2-dark.html')

def home_8(request):
    return render(request, 'home-8.html')

def home_8_dark(request):
    return render(request, 'home-8-dark.html')

def home_9(request):
    return render(request, 'home-9.html')
 
def home_9_dark(request):
    return render(request, 'home-9-dark.html')

def home_10(request):
    return render(request, 'home-10.html')

def home_10_dark(request):
    return render(request, 'home-10-dark.html')

def home_11(request):
    return render(request, 'home-11.html')
def home_11_dark(request):
    return render(request, 'home-11-dark.html')

# index par DOHA Primael 

def index(request):
    return render(request,'index.html')

def index_dark(request):
    return render(request,'index-dark.html')

# instructor par DOHA Primael 

def instructor(request):
    return render(request, 'instructor.html')

def instructor_details(request):
    return render(request, 'instructor-details.html')

def instructor_dark(request):
    return render(request, 'instructor-dark.html')

def instructor_details_dark(request):
    return render(request, 'instructor-details-dark.html')

# lessons par DOHA Primael 

def lesson(request):
    return render(request, 'lesson.html')

def lesson_assignment(request):
    return render(request, 'lesson_assignment.html')

def lesson_course_materials(request):
    return render(request, 'lesson_course_materials.html')

def lesson_quiz(request):
    return render(request, 'lesson_quiz.html')


def lesson_2(request):
    return render(request, 'lesson-2.html')

def lesson_3(request):
    return render(request, 'lesson-3.html')

# login par DOHA Primael 

def login(request):
    return render(request, 'login.html')
def login_dark(request):
    return render(request, 'login-dark.html')


# maintenance par DOHA Primael 

def maintenance(request):
    return render(request, 'maintenance.html')

def maintenance_dark(request):
    return render(request, 'maintenance-dark.html')

# 1212
def base(request):
    return render(request, 'base.html')


# DASHBORD par DOHA Primael 


def admin_course(request):
    return render(request, 'admin-course.html')

def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def admin_message(request):
    return render(request, 'admin-message.html')

def admin_profile(request):
    return render(request, 'admin-profile.html')

def admin_quiz_attempts(request):
    return render(request, 'admin-quiz-attempts.html')

def admin_reviews(request):
    return render(request, 'admin-reviews.html')

def admin_settings(request):
    return render(request, 'admin-settings.html')

def become_an_instructor(request):
    return render(request, 'become-an-instructor.html')

def create_course(request):
    return render(request, 'create-course.html')

def instructor_announcments(request):
    return render(request, 'instructor-announcments.html')

def instructor_assignments(request):
    return render(request, 'instructor-assignments.html')

def instructor_course(request):
    return render(request, 'instructor-course.html')

def instructor_dashboard(request):
    return render(request, 'instructor-dashboard.html')

def instructor_message(request):
    return render(request, 'instructor-message.html')

def instructor_my_quiz_attempts(request):
    return render(request, 'instructor-my-quiz-attempts.html')

def instructor_order_history(request):
    return render(request, 'instructor-order-history.html')

def instructor_profile(request):
    return render(request, 'instructor-profile.html')

def instructor_quiz_attempts(request):
    return render(request, 'instructor-quiz-attempts.html')

def instructor_reviews(request):
    return render(request, 'instructor-reviews.html')

def instructor_settings(request):
    return render(request, 'instructor-settings.html')

def instructor_wishlist(request):
    return render(request, 'instructor-wishlist.html')




def student_assignments(request):
    return render(request, 'student-assignments.html')

def student_dashboard(request):
    return render(request, 'student-dashboard.html')

def student_enrolled_courses(request):
    return render(request, 'student-enrolled-courses.html')

def student_message(request):
    return render(request, 'student-message.html')

def student_my_quiz_attempts(request):
    return render(request, 'student-my-quiz-attempts.html')


def student_profile(request):
    return render(request, 'student-profile.html')

def student_reviews(request):
    return render(request, 'student-reviews.html')

def student_settings(request):
    return render(request, 'student-settings.html')

def student_wishlist(request):
    return render(request, 'student-wishlist.html')



# E-COMMERCE par DOHA Primael 
def cart(request):
    return render(request, 'cart.html')

def cart_dark(request):
    return render(request, 'cart-dark.html')

def checkout(request):
    return render(request, 'checkout.html')

def checkout_dark(request):
    return render(request, 'checkout-dark.html')

def product_details(request):
    return render(request, 'product-details.html')

def product_details_dark(request):
    return render(request, 'product-details-dark.html')

def shop(request):
    return render(request, 'shop.html')

def shop_dark(request):
    return render(request, 'shop-dark.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def wishlist_dark(request):
    return render(request, 'wishlist-dark.html')


# ZOOM par DOHA Primael 

def zoom_meeting_details(request):
    return render(request, 'zoom-meeting-details.html')

def zoom_meeting_details_dark(request):
    return render(request, 'zoom-meeting-details-dark.html')

def zoom_meeting(request):
    return render(request, 'zoom-meetings.html')

def zoom_meeting_dark(request):
    return render(request, 'zoom-meetings-dark.html')





@login_required
def dashboard(request):
    if request.user.status == 'mentor':
        # Charger les données spécifiques au mentor (instructeur)
        courses = request.user.instructed_courses.all()  # Cours enseignés par le mentor
        statistics = Statistic.objects.filter(user=request.user)  # Statistiques du mentor
        context = {
            'courses': courses,
            'statistics': statistics,
        }
        return render(request, 'dashboard_instructor.html', context)

    elif request.user.status == 'apprenant':
        # Charger les données spécifiques à l'apprenant (étudiant)
        enrollments = Enrollment.objects.filter(user=request.user)  # Cours inscrits par l'étudiant
        certificates = Certificate.objects.filter(user=request.user)  # Certificats de l'étudiant
        context = {
            'enrollments': enrollments,
            'certificates': certificates,
        }
        return render(request, 'dashboard_student.html', context)
    
    else:
        # Optionnel : Si un autre type d'utilisateur existe, gérer ici
        return render(request, 'dashboard_default.html', {'user': request.user})
















