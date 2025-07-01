document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.confirm-delete').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (!confirm('Are you sure you want to delete this post?')) {
        e.preventDefault();
      }
    });
  });
});