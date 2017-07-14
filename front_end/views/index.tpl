% include('header.tpl')
<div class="container">
  <div class="card mx-auto" style="width: 25rem; margin-top: 50px;">
    <img class="card-img-top img-fluid" src="/images/{{main_pic}}" alt="What I look like.">
    <div class="card-header">
      <ul class="nav nav-tabs card-header-tabs">
        <li class="nav-item">
          <a class="nav-link active" href="#about">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#resume">Resume</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#social">Social</a>
        </li>
      </ul>
    </div> <!-- card header -->
    <div class="card-block">
      <h4 class="card-title"><span class="text-muted">Hi, I'm</span> {{name}}.</h4>
      <p class="card-text">
        <p class="lead special-font"><small>{{header_quotation}}</small></p>
        <h5><small>{{blurb}}</small></h5>
      </p>
    </div> <!-- card block -->
    <div class="card-footer">
      <div class="row">
        <div class="col">
          <a target="_blank" href="{{gdoc_URL}}"  role="button" data-toggle="tooltip" data-placement="bottom" title="Go to Google doc, or download directly">
            <img src="/images/docs.png" class="img-fluid" style="height: 48px;">
          </a>
        </div> <!-- col -->
        <div class="col">
          <a target="_blank" href="{{github_URL}}"  role="button" data-toggle="tooltip" data-placement="bottom" title="Check out my GitHub">
            <img src="/images/github-cat.svg" class="img-fluid" style="height: 48px";>
          </a>
        </div> <!-- col -->
        <div class="col">
          <a target="_blank" href="{{linkedin_URL}}"  role="button" data-toggle="tooltip" data-placement="bottom" title="Connect with me on Linkedin">
            <img src="/images/linkedin.svg" class="img-fluid" style="height: 48px";>
          </a>
        </div> <!-- col -->
        </div> <!-- row -->
    </div> <!-- card footer -->
  </div> <!-- card -->

% include('footer.tpl')
