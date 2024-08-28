# myapp/context_processors.py

from .models import *

def dashboard_context(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.status == 'apprenant':
            user = request.user
            # Données pour les apprenants
            enrolled_courses = Enrollment.objects.filter(user=user)
            active_courses = enrolled_courses.filter(active=True)
            completed_courses = Certificate.objects.filter(user=user)
            feedbacks = Feedback.objects.filter(user=user)
            quiz_attempts = QuizAttempt.objects.filter(user=user)
            assignments = Assignment.objects.filter(course__in=enrolled_courses.values_list('course', flat=True))
            unread_messages_count = Message.objects.filter(recipient=user, read=False).count()


            context.update({
            'user': user,
            'enrolled_courses': enrolled_courses,
            'active_courses': active_courses,
            'completed_courses': completed_courses,
            'feedbacks': feedbacks,
            'quiz_attempts': quiz_attempts,
            'assignments': assignments,
            'unread_messages_count': unread_messages_count,
            'range_five': range(1, 6),  # Ajout de la plage range(1, 6) au contexte
            })

        elif request.user.status == 'mentor':
            # Données pour les mentors
            instructor = request.user
            instructor_courses = Course.objects.filter(instructor=instructor)
            total_courses = instructor_courses.count()
            active_courses = instructor_courses.filter(status='active').count()
            completed_courses = instructor_courses.filter(status='completed').count()
            total_students = sum(course.students.count() for course in instructor_courses)
            total_earnings = sum(course.total_points for course in instructor_courses)
            testimonials = ClientTestimonial.objects.all()
            awards = Award.objects.all()

            context.update({
                'instructor': instructor,
                'total_courses': total_courses,
                'active_courses': active_courses,
                'completed_courses': completed_courses,
                'total_students': total_students,
                'total_earnings': total_earnings,
                'testimonials': testimonials,
                'awards': awards,
            })

    return context
