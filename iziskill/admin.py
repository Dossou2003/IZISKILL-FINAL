from django.contrib import admin
from .models import User, Profile, Course, Statistic, Enrollment, Certificate, Feedback, Message, Wishlist, QuizAttempt, Assignment, UserSetting, InstructorDashboard,ClientTestimonial, Award,Category,Panier,PaymentRecord


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','username', 'is_active','is_staff' , 'status', 'points', 'image') 
    search_fields = ('username', 'email')
    list_filter = ('status',)
    ordering = ('username',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'birth_date')
    search_fields = ('user__username',)

# ADMIN PAR PRIMAEL DOHA 
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'total_points')
    search_fields = ('title', 'instructor__username')
    list_filter = ('instructor',)
    filter_horizontal = ('students',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'quantity', 'total_price', 'added_at')
    search_fields = ('user__username', 'course__title')
    list_filter = ('user', 'course', 'added_at')

    def total_price(self, obj):
        return f"{obj.total_price} €"
    total_price.short_description = 'Prix Total'

class PaymentRecordAdmin(admin.ModelAdmin):
    # Colonnes à afficher dans la liste des enregistrements
    list_display = ('user', 'course', 'amount', 'email', 'payment_date')
    
    # Colonnes sur lesquelles on peut filtrer
    list_filter = ('payment_date', 'course')
    
    # Champs de recherche
    search_fields = ('user__username', 'user__first_name', 'user__email', 'course__name')
    
    # Champs à utiliser pour l'ordre par défaut
    ordering = ('-payment_date',)

# Enregistrer le modèle avec cette configuration dans l'administration
admin.site.register(PaymentRecord, PaymentRecordAdmin)

# FIN

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('user', 'enrolled_courses', 'active_courses', 'completed_courses')
    search_fields = ('user__username',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at', 'active')
    search_fields = ('user__username', 'course__title')
    list_filter = ('active',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'issue_date', 'certificate_number')
    search_fields = ('user__username', 'course__title', 'certificate_number')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating')
    search_fields = ('user__username', 'course__title')
    list_filter = ('rating',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp', 'read')
    search_fields = ('sender__username', 'recipient__username')
    list_filter = ('read',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    search_fields = ('user__username', 'course__title')

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'score', 'attempt_date')
    search_fields = ('user__username', 'course__title')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'due_date')
    search_fields = ('title', 'course__title')
    list_filter = ('due_date',)

@admin.register(UserSetting)
class UserSettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'receive_notifications', 'dark_mode')
    search_fields = ('user__username',)


@admin.register(InstructorDashboard)
class InstructorDashboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_courses', 'total_students', 'total_earnings')
    search_fields = ('user__username',)
    
    




from django.contrib import admin
from .models import Video, MentoringSession, Payment, MentoringRequest

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'video_file')
    list_filter = ('course',)
    search_fields = ('title', 'course__title')
    ordering = ('course', 'order')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(MentoringSession)
class MentoringSessionAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'learner', 'course', 'session_date', 'duration', 'price_per_hour')
    list_filter = ('mentor', 'learner', 'course', 'session_date')
    search_fields = ('mentor__username', 'learner__username', 'course__title')
    ordering = ('session_date',)
    raw_id_fields = ('mentor', 'learner', 'course')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'session', 'amount', 'payment_date', 'successful')
    list_filter = ('user', 'course', 'session', 'successful')
    search_fields = ('user__username', 'course__title', 'session__mentor__username')
    ordering = ('-payment_date',)
    raw_id_fields = ('user', 'course', 'session')

@admin.register(MentoringRequest)
class MentoringRequestAdmin(admin.ModelAdmin):
    list_display = ('learner', 'course', 'preferred_date', 'status')
    list_filter = ('learner', 'course', 'status')
    search_fields = ('learner__username', 'course__title')
    ordering = ('-preferred_date',)
    raw_id_fields = ('learner', 'course')




@admin.register(ClientTestimonial)
class ClientTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'rating', 'created_at')
    list_filter = ('profession', 'rating')
    search_fields = ('name', 'profession', 'comment')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fields = ('image', 'name', 'profession', 'comment', 'rating', 'created_at')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'award_date')
    search_fields = ('title', 'description')
    ordering = ('-award_date',)
    fields = ('title', 'description', 'image', 'award_date')