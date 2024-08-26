
from django.contrib import admin
from django.urls import path
from iziskill import views


from django.conf.urls.static import static

from techseed import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #  about par DOHA Primael

    path('about/',views.about, name="about"),

    path('about_dark/',views.about_dark, name="about_dark"),

    # blog DOHA Primael
    path('blog/',views.blog, name="blog"),

    path('blog_dark/',views.blog_dark, name="blog_dark"),

    path('blog_details/',views.blog_details, name="blog_details"),

    path('blog_details_dark/',views.blog_details_dark, name="blog_details_dark"),
     
     # contact par DOHA Primael 
    path('contact/',views.contact, name="contact"),

    path('contact_dark/',views.contact_dark, name="contact_dark"),
    
    # course par DOHA Primael
    path('course/',views.course, name="course"),

    path('course_dark/',views.course_dark, name="course_dark"),

    path('courses_details/',views.courses_details, name="courses_details"),

    path('courses_details_dark/',views.courses_details_dark, name="courses_details_dark"),

    path('courses_details_2/',views.courses_details_2, name="courses_details_2"),

    path('courses_details_3/',views.courses_details_3, name="courses_details_3"),

    path('courses_details_2_dark/',views.courses_details_2_dark, name="courses_details_2_dark"),

    path('courses_details_3_dark/',views.courses_details_3_dark, name="courses_details_3_dark"),

    path('courses_grid/',views.courses_grid, name="courses_grid"),

    path('courses_grid_dark/',views.courses_grid_dark, name="courses_grid_dark"),

    path('course_list/',views.course_list, name="course_list"),

    path('course_list_dark/',views.course_list_dark, name="course_list_dark"),

    # error par DOHA Primael 
    path('error/',views.error, name="error"),

    path('error_dark/',views.error_dark, name="error_dark"),

   
    # event par DOHA Primael
    path('event_details/',views.event_details, name="event_details"),

    path('event_details_dark/',views.event_details_dark, name="event_details_dark"),
    
    #home par DOHA Primael
    path('home_2/',views.home_2, name="home_2"),

    path('home_2_dark/',views.home_2_dark, name="home_2_dark"),

    path('home_3/',views.home_3, name="home_3"),

    path('home_3_dark/',views.home_3_dark, name="home_3_dark"),

    path('home_4/',views.home_4, name="home_4"),

    path('home_4_dark/',views.home_4_dark, name="home_4_dark"),

    path('',views.home_5, name="home_5"),

    path('home_5_dark/',views.home_5_dark, name="home_5_dark"),

    path('home_6/',views.home_6, name="home_6"),

    path('home_6_dark/',views.home_6_dark, name="home_6_dark"),

    path('home_7/',views.home_7, name="home_7"),

    path('home_7_dark/',views.home_7_dark, name="home_7_dark"),

    path('home_8/',views.home_8, name="home_8"),

    path('home_8_dark/',views.home_8_dark, name="home_8_dark"),

    path('home_9/',views.home_9, name="home_9"),

    path('home_9_dark/',views.home_9_dark, name="home_9_dark"),

    path('home_10/',views.home_10, name="home_10"),

    path('home_10_dark/',views.home_10_dark, name="home_10_dark"),

    path('home_11/',views.home_11, name="home_11"),

    path('home_11_dark/',views.home_11_dark, name="home_11_dark"),
    
    # index par DOHA Primael 
    path('index/',views.index, name="index"),

    path('index_dark/',views.index_dark, name="login"),

    # instructor par DOHA Primael 
    path('instructor/',views.instructor, name="instructor"),

    path('instructor_details/',views.instructor_details, name="instructor_details"),
    
    path('instructor_dark',views.instructor_dark, name="instructor_dark"),

    path('instructor_details_dark/',views.instructor_details_dark, name="instructor_details_dark"),

   
   # lessons par DOHA Primael 
    path('lesson/',views.lesson, name="lesson"),

    path('lesson_assignment/',views.lesson_assignment, name="lesson_assignment"),

    path('lesson_course_materials/',views.lesson_course_materials, name="lesson_course_materials"),

    path('lesson_quiz/',views.lesson_quiz, name="lesson_quiz"),

    path('lesson_2/',views.lesson_2, name="lesson_2"),

    path('lesson_3/',views.lesson_3, name="lesson_3"),

    # login par DOHA Primael 
    path('login/',views.login, name="login"),

    path('login_dark/',views.login_dark, name="login_dark"),
    
    # maintenance par DOHA Primael 
    path('maintenance/',views.maintenance, name="maintenance"),

    path('maintenance_dark/',views.maintenance_dark, name="maintenance_dark"),

   
    path('base/',views.base, name="base"),
    

    # DASHBORD par DOHA Primael 

    path('admin_course/',views.admin_course, name="admin_course"),

    path('admin_dashboard/',views.admin_dashboard, name="admin_dashboard"),

    path('admin_message/',views.admin_message, name="admin_message"),

    path('admin_profile/',views.admin_profile, name="admin_profile"),

    path('admin_quiz_attempts/',views.admin_quiz_attempts, name="admin_quiz_attempts"),

    path('admin_reviews/',views.admin_reviews, name="admin_reviews"),

    path('admin_settings/',views.admin_settings, name="admin_settings"),

    path('become_an_instructor/',views.become_an_instructor, name="become_an_instructor"),

    path('create_course/',views.create_course, name="create_course"),

    path('instructor_announcments/',views.instructor_announcments, name="instructor_announcments"),

    path('instructor_assignments/',views.instructor_assignments, name="instructor_assignments"),

    path('instructor_course/',views.instructor_course, name="instructor_course"),

    path('instructor_dashboard/',views.instructor_dashboard, name="instructor_dashboard"),

    path('instructor_message/',views.instructor_message, name="instructor_message"),

    path('instructor_my_quiz_attempts/',views.instructor_my_quiz_attempts, name="instructor_my_quiz_attempts"),

    path('instructor_order_history/',views.instructor_order_history, name="instructor_order_history"),

    path('instructor_profile/',views.instructor_profile, name="instructor_profile"),

    
    path('instructor_quiz_attempts/',views.instructor_quiz_attempts, name="instructor_quiz_attempts"),

    path('instructor_reviews/',views.instructor_reviews, name="instructor_reviews"),

    path('instructor_settings/',views.instructor_settings, name="instructor_settings"),

    path('instructor_wishlist/',views.instructor_wishlist, name="instructor_wishlist"),

    path('student_assignments/',views.student_assignments, name="student_assignments"),

    path('student_dashboard/',views.student_dashboard, name="student_dashboard"),

    path('student_enrolled_courses/',views.student_enrolled_courses, name="student_enrolled_courses"),

    path('student_message/',views.student_message, name="student_message"),

    path('student_my_quiz_attempts/',views.student_my_quiz_attempts, name="student_my_quiz_attempts"),

    path('student_profile/',views.student_profile, name="student_profile"),

    path('student_reviews/',views.student_reviews, name="student_reviews"),

    path('student_settings/',views.student_settings, name="student_settings"),

    path('student_wishlist/',views.student_wishlist, name="student_wishlist"),

    
# E-COMMERCE par DOHA Primael 
    path('cart/',views.cart, name="cart"),

    path('cart_dark/',views.cart_dark, name="cart_dark"),

    path('checkout/',views.checkout, name="checkout"),

    path('checkout_dark/',views.checkout_dark, name="checkout_dark"),

    path('product_details/',views.product_details, name="product_details"),

    path('product_details_dark/',views. product_details_dark, name=" product_details_dark"),

    path('shop/',views.shop, name="shop"),

    path('shop_dark/',views.shop_dark, name="shop_dark"),

    path('wishlist/',views.wishlist, name="wishlist"),

    path('wishlist_dark/',views.wishlist_dark, name="wishlist_dark"),

# ZOOM par DOHA Primael 

    path('zoom_meeting_details/',views.zoom_meeting_details, name="zoom_meeting_details"),

    path('zoom_meeting_details_dark/',views.zoom_meeting_details_dark, name="zoom_meeting_details_dark"),

    path('zoom_meeting/',views.zoom_meeting, name="zoom_meeting"),

    path('zoom_meeting_dark/',views.zoom_meeting_dark, name="zoom_meeting_dark"),









    



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

