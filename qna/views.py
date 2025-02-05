from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Issue, Reply, Vote
from .forms import CustomUserCreationForm, IssueForm, ReplyForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'qna/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('index')  # Redirect to the homepage or wherever you want
            else:
                form.add_error(None, "Invalid credentials")  # Add error if authentication fails
    else:
        form = AuthenticationForm()

    return render(request, 'qna/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    query = request.GET.get('q', '') 
    selected_tag = request.GET.get('tag', '') 
    
    issues = Issue.objects.all().order_by('-created_at')  # Sort by newest first

    if query:
        issues = issues.filter(title__icontains=query) 

    if selected_tag:
        issues = issues.filter(tags=selected_tag)  

    return render(request, 'qna/index.html', {'issues': issues, 'query': query, 'selected_tag': selected_tag})

@login_required(login_url='/login/')
def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    replies = issue.replies.all().order_by('-upvotes')

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.issue = issue
            reply.author = request.user
            reply.save()
            return redirect('issue_detail', issue_id=issue.id)
    else:
        form = ReplyForm()

    return render(request, 'qna/issue_detail.html', {'issue': issue, 'replies': replies, 'form': form})


@login_required(login_url='/login/')
def create_issue(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.get('tags')

        errors = {}

        # Custom validation for title
        if not title:
            errors['title'] = 'Title is required.'

        # Custom validation for description
        if not description:
            errors['description'] = 'Description is required.'

        # Custom validation for tags (optional)
        if not tags:
            errors['tags'] = 'Tags are required.'

        # If there are any errors, redirect to the error page
        if errors:
            return render(request, 'qna/error.html', {'errors': errors})

        # If no errors, save the issue
        issue = Issue.objects.create(
            title=title,
            description=description,
            tags=tags,
            author=request.user
        )
        return redirect('index')

    return render(request, 'qna/create_issue.html')


@login_required(login_url='/login/')
def add_reply(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    errors = {}
    
    if request.method == 'POST':
        content = request.POST.get('content')
        
        # Basic validation for reply content
        if not content:
            errors['content'] = 'Reply content is required.'

        # If errors exist, render the issue_detail template with errors
        if errors:
            return render(request, 'qna/issue_detail.html', {'issue': issue, 'errors': errors})
        
        # Save the reply if no errors
        reply = Reply.objects.create(
            content=content,
            issue=issue,
            author=request.user
        )
        return redirect('issue_detail', issue_id=issue.id)

    return render(request, 'qna/issue_detail.html', {'issue': issue, 'errors': errors})
@login_required(login_url='/login/')
def close_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    
    # Ensure the current user is the author of the issue
    if issue.author == request.user:
        issue.is_solved = True
        issue.save()
    
    return redirect('issue_detail', issue_id=issue.id)


@login_required(login_url='/login/')
def vote(request, reply_id, vote_type):
    if vote_type not in ['up', 'down']:
        return JsonResponse({'success': False})

    reply = get_object_or_404(Reply, id=reply_id)
    user = request.user

    # Check if the user has already voted on this reply
    existing_vote = Vote.objects.filter(user=user, reply=reply).first()
    
    if existing_vote:
        if existing_vote.vote_type == vote_type:
            # If the user is removing their vote
            existing_vote.delete()
        else:
            # If the user is changing their vote
            existing_vote.vote_type = vote_type
            existing_vote.save()
    else:
        # Create a new vote if the user hasn't voted on this reply
        Vote.objects.create(user=user, reply=reply, vote_type=vote_type)

    # Update the upvotes and downvotes count based on the votes
    reply.upvotes = Vote.objects.filter(reply=reply, vote_type='up').count()
    reply.downvotes = Vote.objects.filter(reply=reply, vote_type='down').count()
    reply.save()

    # Return the updated vote counts as a JSON response
    return JsonResponse({
        'success': True,
        'upvotes': reply.upvotes,
        'downvotes': reply.downvotes
    })


def profile(request, username):
    user = get_object_or_404(User, username=username)  # Get user by username
    issues = Issue.objects.filter(author=user).order_by('-created_at')
    return render(request, 'qna/profile.html', {'user': user, 'issues': issues})