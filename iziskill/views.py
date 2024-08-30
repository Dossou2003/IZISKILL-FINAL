from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from iziskill.models import *


from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.db import models
from django.utils.encoding import force_str
from .models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse
from .tokens import account_activation_token
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .forms import CustomPasswordResetForm, CustomSetPasswordForm
from django.contrib.auth.decorators import login_required
from django.conf import settings



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Désactiver le compte jusqu'à l'activation
            user.save()

            # Générer le jeton d'activation
            current_site = get_current_site(request)
            mail_subject = 'Activez votre compte.'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(mail_subject, message, 'from@example.com', [user.email])

            messages.success(request, "Un email d'activation a été envoyé à votre adresse email. Cliquez sur le lien pour activer votre compte")
            return redirect('login')
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})




def login_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        username = form.data.get('username')
        password = form.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None:
            if user.is_active:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Bienvenue {user.first_name} !")
                    if user.status == 'apprenant':
                        return redirect('student_dashboard')
                    elif user.status == 'mentor':
                        return redirect('instructor_dashboard')
                else:
                    messages.error(request, "Mot de passe incorrect.")
            else:
                messages.error(request, "Votre compte n'est pas encore activé. Veuillez vérifier votre email pour l'activer.")
        else:
            messages.error(request, "Identifiant incorrect.")
    
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



User = get_user_model()

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Votre compte a été activé avec succès.')
        return redirect('login')
    else:
        messages.error(request, 'Le lien d\'activation est invalide.')
        return redirect('register')
    

def password_reset_request(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            subject = "Réinitialisation du mot de passe"
            message = render_to_string('password_reset_email.html', {
                'user': user,
                'domain': domain,
                'uid': uid,
                'token': token,
            })
            send_mail(subject, message, 'from@example.com', [email])
            messages.success(request, "Un email de réinitialisation du mot de passe a été envoyé.")
            return redirect('password_reset_done')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})





def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = CustomSetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Votre mot de passe a été réinitialisé avec succès.")
                return redirect('login')
        else:
            form = CustomSetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Le lien de réinitialisation du mot de passe est invalide.")
        return redirect('password_reset')
    
    
    

def password_reset_done(request):
    return render(request, 'password_reset_done.html')



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
# PAR PRIMAEL DOHA 

def course_list(request):
    courses = Course.objects.all()  # Récupère tous les objets Course
    for course in courses:
        if not course.image:
            # Gérer les cas où il n'y a pas d'image associée
            course.image_url = None
        else:
            course.image_url = course.image.url
    return render(request, 'course-list.html', {'courses': courses})

def courses_details(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course-details.html', {'course': course})

def panier_view(request):
    paniers = Panier.objects.filter(user=request.user)
    total = sum(item.total_price for item in paniers)
    
    return render(request, 'panier.html', {'paniers': paniers, 'total': total})

def ajouter_au_panier(request, course_id):
    course = Course.objects.get(id=course_id)
    panier, created = Panier.objects.get_or_create(user=request.user, course=course)
    
    if not created:
        panier.quantity += 1
        panier.save()
    
    return panier



            
def ajouter_au_panier_view(request, course_id):
    ajouter_au_panier(request, course_id)
    return redirect('cart')

def supprimer_du_panier(request, course_id):
    course = Course.objects.get(id=course_id)
    panier = Panier.objects.filter(user=request.user, course=course).first()
    
    if panier:
        if panier.quantity > 1:
            panier.quantity -= 1
            panier.save()
        else:
            panier.delete()
            
def supprimer_du_panier_view(request, course_id):
    supprimer_du_panier(request, course_id)
    return redirect('cart')

def payment(request):
    paniers = Panier.objects.filter(user=request.user)
    total = sum(item.total_price for item in paniers)
    return render(request, 'payment.html', {'paniers': paniers, 'total': total, 'course': course})

def cart(request):
    courses = Course.objects.all()  # Récupère tous les objets Course
    for course in courses:
        if not course.image:
            # Gérer les cas où il n'y a pas d'image associée
            course.image_url = None
        else:
            course.image_url = course.image.url

    paniers = Panier.objects.filter(user=request.user)
    total = sum(item.total_price for item in paniers)
    
    
    return render(request, 'cart.html', {'paniers': paniers, 'total': total, 'courses' : courses})
    

def cart_dark(request):
    return render(request, 'cart-dark.html')




#####

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



# =================pour les extends=============================

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






from django.shortcuts import render, redirect
from .models import User, Course, ClientTestimonial, Award

def instructor_dashboard(request):
    if request.user.is_authenticated and request.user.status == 'mentor':
        instructor = request.user

        # Données de l'instructeur
        instructor_courses = Course.objects.filter(instructor=instructor)
        total_courses = instructor_courses.count()
        active_courses = instructor_courses.filter(  # Assurez-vous d'avoir un champ 'status' dans votre modèle Course
            status='active'  
        ).count()
        completed_courses = instructor_courses.filter(
            status='completed'  
        ).count()
        total_students = sum(course.students.count() for course in instructor_courses)
        total_earnings = (
            sum(course.total_points for course in instructor_courses)
            # Ou calculez les gains réels si vous avez cette information dans votre modèle
        )

        # Témoignages des clients
        testimonials = ClientTestimonial.objects.all()  # Ou filtrez si nécessaire

        # Récompenses
        awards = Award.objects.filter(  # Vous pourriez vouloir filtrer par instructeur si nécessaire
            # ... 
        )

        context = {
            'instructor': instructor,
            'total_courses': total_courses,
            'active_courses': active_courses,
            'completed_courses': completed_courses,
            'total_students': total_students,
            'total_earnings': total_earnings,
            'testimonials': testimonials,
            'awards': awards,
        }
        return render(request, 'instructor_dashboard.html', context)
    else:
        return redirect('login')










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
    if request.user.is_authenticated and request.user.status == 'apprenant':
        user = request.user
        
        # Récupérer les données pour le tableau de bord de l'apprenant
        enrolled_courses = Enrollment.objects.filter(user=user)
        active_courses = enrolled_courses.filter(active=True)
        completed_courses = Certificate.objects.filter(user=user)
        feedbacks = Feedback.objects.filter(user=user)
        quiz_attempts = QuizAttempt.objects.filter(user=user)
        assignments = Assignment.objects.filter(course__in=enrolled_courses.values_list('course', flat=True))
        unread_messages_count = Message.objects.filter(recipient=user, read=False).count()

        context = {
            'user': user,
            'enrolled_courses': enrolled_courses,
            'active_courses': active_courses,
            'completed_courses': completed_courses,
            'feedbacks': feedbacks,
            'quiz_attempts': quiz_attempts,
            'assignments': assignments,
            'unread_messages_count': unread_messages_count,
            'range_five': range(1, 6),  # Ajout de la plage range(1, 6) au contexte
        }
        return render(request, 'student_dashboard.html', context)
    else:
        # Rediriger si l'utilisateur n'est pas authentifié ou n'est pas un apprenant
        return redirect('login')






def student_enrolled_courses(request):
    return render(request, 'student-enrolled-courses.html')
@login_required
def student_message(request):
    return render(request, 'student-message.html')

def student_my_quiz_attempts(request):
    return render(request, 'student-my-quiz-attempts.html')

@login_required
def student_profile(request):
    user = request.user
    return render(request, 'student-profile.html', {'user':user})

def student_reviews(request):
    return render(request, 'student-reviews.html')

def student_settings(request):
    return render(request, 'student-settings.html')

def student_wishlist(request):
    return render(request, 'student-wishlist.html')



# E-COMMERCE par DOHA Primael 


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