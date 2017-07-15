% include('header.tpl')
<div class="container align-self-center">
<div class="row justify-content-center">
<div class="col-xl-8 col-lg-9 col-md-11 col-sm-12">
  <div class="card mx-auto" style="width: 475px;">
    <img class="img-fluid" src="/images/{{main_pic}}"  alt="What I look like.">
      <div class="card-img-overlay">
        <pre class="top-desc">
          {{name.upper()}} = {'occupation': '{{occupation}}',
          % final_item = len(skills) - 1
          % for i, skill in enumerate(skills):
          %     if i == 0:   
                   'skills': ['{{skill}}',
          %     end
          %     if i == final_item:
                              '{{skill}}'],
          %     end
          %     if i != final_item and i != 0:
                              '{{skill}}',
          %     end
          % end
          % final_item = len(likes) - 1
          % for i, like in enumerate(likes):
          %     if i == 0:   
                   'likes': ['{{like}}',
          %     end
          %     if i == final_item:
                             '{{like}}']}
          %     end
          %     if i != final_item and i != 0:
                             '{{like}}',
          %     end
          % end
        </pre>
    </div>
    <div class="card-header">
      <ul class="nav nav-tabs card-header-tabs">
        <li class="nav-item">
          <a class="nav-link active" href="#about">About</a>
        </li>
        <li class="nav-item">
          <div class="dropdown">
            <button class="dropdown-toggle border-0" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <img src="/images/googledocs.svg" class="img-fluid docs-img">Resume
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="menu-drop-item" target="_blank" href="{{gdoc_URL}}"  role="button" data-toggle="tooltip" data-placement="bottom" title="Go to Google doc, or download directly">Live Doc</a>
            <h6 class="dropdown-header">Direct Downloads</h6>
              <a class="menu-drop-item" href="{{resume_pdf_URL}}">Download .PDF</a>
              <a class="menu-drop-item" href="{{resume_docx_URL}}">Download .Docx</a>
            </div>
          </div>
        </li>
      </ul>
    </div> <!-- card header -->
    <div class="card-block">
      <h4 class="card-title"><span class="text-muted">Hi, I'm</span> {{name}}.</h4>
      <p class="card-text">
        {{blurb}}
      </p>
    </div> <!-- card block -->
    <div class="card-footer">
      <div class="row justify-content-between">
        <div class="col-6">
          <a target="_blank" href="{{github_URL}}"  role="button" data-toggle="tooltip" data-placement="bottom" title="Check out my GitHub">
            <img src="/images/github-cat.svg" class="img-fluid" style="height: 48px";>
          </a>
        </div> <!-- col -->
        <div class="col-6">
          <a target="_blank" href="{{linkedin_URL}}"  role="button" data-toggle="tooltip" data-placement="bottom" title="Connect with me on Linkedin">
            <img src="/images/linkedin.svg" class="img-fluid" style="height: 48px";>
          </a>
        </div> <!-- col -->
        </div> <!-- row -->
    </div> <!-- card footer -->
  </div> <!-- card -->
</div> <!-- col -->
</div> <!-- row -->

% include('footer.tpl')
