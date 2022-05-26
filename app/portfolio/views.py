from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import JsonResponse
from app.portfolio.helpers.tasks import send_mail_

from app.portfolio.models import (
    AboutImages,
    Category,
    Email,
    ExtraImage,
    Profile,
    Project,
    Service,
    Socials,
)


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        projects = Project.objects.all()
        categories = Category.objects.all()
        socials = Socials.objects.all()
        profile = Profile.objects.first()
        services = Service.objects.all()
        extra_images = ExtraImage.objects.all()
        return render(
            request,
            self.template_name,
            context={
                "projects": projects,
                "categories": categories,
                "socials": socials,
                "profile": profile,
                "services": services,
                "extra_images": extra_images,
            },
        )


class ProjectView(TemplateView):
    template_name = "project.html"

    def get(self, request, project_name):
        socials = Socials.objects.all()
        project = Project.objects.get(slug__iexact=project_name)
        return render(
            request,
            self.template_name,
            context={"project": project, "socials": socials},
        )


class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request):
        socials = Socials.objects.all()
        return render(request, self.template_name, context={"socials": socials})

    def post(self, request):
        data = request.POST
        email_data = {
            "name": data["name"],
            "email": data["email"],
            "message": data["message"],
        }
        mail = Email(**email_data)
        mail.save()
        send_mail_.delay(
            f"Message from portfolio! - | {mail.name} |-| {mail.email} |",
            mail.message,
            mail.email,
        )

        return JsonResponse(
            {"message": "Email sent successfully. I will be in contact ASAP"}
        )


class AboutView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        socials = Socials.objects.all()
        profile = Profile.objects.first()
        categories = Category.objects.all()
        services = Service.objects.all()
        about_images = AboutImages.objects.first()

        return render(
            request,
            self.template_name,
            context={
                "socials": socials,
                "profile": profile,
                "categories": categories,
                "services": services,
                "about_images": about_images,
            },
        )
