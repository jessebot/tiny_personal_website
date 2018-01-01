% include('header.tpl')
<div class="container">
  <div class="row d-flex justify-content-center align-items-center">
  <div class="col-7 col-lg-4 col-md-4 col-sm-7 col-xl-4 pb-1 m-1">
    <img class="img-fluid rounded main-img"
         src="/images/{{globals['image']}}"
         alt="What I look like.">
  </div>
  <div class="col-10 col-sm-10 col-md-8 col-lg-6 offset-lg-1 offset-xl-1 pt-2 pb-2">
  <div class="card mx-auto">
    <div class="card-header">
      <ul class="nav nav-tabs card-header-tabs">
        <li class="nav-item">
          <a class="nav-link active" href="#about">About</a>
        </li>
        <li class="nav-item">
          <div class="dropdown">
            <button class="dropdown-toggle border-0" 
                    type="button" id="dropdownMenuButton"
                    data-toggle="dropdown"
                    aria-haspopup="true" aria-expanded="false">
              <img src="/images/googledocs.svg" 
              class="img-fluid docs-img">Resume
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="menu-drop-item" target="_blank"
                 href="{{globals['resume_live_doc_URL']}}" role="button"
                 data-toggle="tooltip" data-placement="right"
                 title="Google doc">Live Doc</a>
            <h6 class="dropdown-header">Direct Downloads</h6>
              <a class="menu-drop-item"
                 href="{{globals['resume_pdf_URL']}}">Download .PDF</a>
              <a class="menu-drop-item"
                 href="{{globals['resume_docx_URL']}}">Download .Docx</a>
            </div> <!-- dropdown-menu -->
          </div> <!-- dropdown -->
        </li>
      </ul>
    </div> <!-- card header -->
    <div class="card-block">
      <h4 class="card-title">
        <span class="text-muted">Hi, I'm</span> {{globals['name']}}.
      </h4>
      <p class="card-text">
        {{globals['profile_blurb']}}
      </p>
    </div> <!-- card block -->
    <div class="card-footer">
      <div class="row justify-content-between">
        <div class="col-6">
          <div class="circle">
            <a target="_blank" href="{{globals['github_URL']}}"
               role="button" data-toggle="tooltip" data-placement="right"
               title="GitHub" style="box-shadow: none;">
              <img src="/images/github-cat.svg" class="img-fluid"
                   style="height: 54px;">
            </a>
          </div> <!-- circle -->
        </div> <!-- col -->
        <div class="col-6">
          <div class="circle">
            <a target="_blank" href="{{globals['linkedin_URL']}}"
               role="button" data-toggle="tooltip" data-placement="left"
               title="Linkedin" style="box-shadow: none;">
              <img src="/images/linkedin.svg" class="img-fluid" style="height: 54px;">
            </a>
          </div><!-- circle -->
        </div> <!-- col -->
      </div> <!-- row -->
    </div> <!-- card footer -->
  </div> <!-- card -->
  </div> <!-- col -->
  </div> <!-- row -->
</div> <!-- container -->

% include('footer.tpl')
