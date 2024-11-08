
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateTaskStatus(taskId, checkbox) {
    const csrfToken = getCookie('csrftoken');
    fetch(`/tasks/update_status/${taskId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            'completed': checkbox.checked
        })
    }).then(response => {
        if (!response.ok) {
            alert('Failed to update task status.');
        }
    });
}

function deleteTask(taskId) {
    const csrfToken = getCookie('csrftoken');
    fetch(`/tasks/delete/${taskId}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken
        }
    }).then(response => response.json())
      .then(data => {
          if (data.status === 'success') {
              const taskElement = document.getElementById(`task-${taskId}`);
              taskElement.remove();
          } else {
              alert('Failed to delete task.');
          }
      });
}