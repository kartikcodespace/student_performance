/**
 * main.js — EduPredict Student Performance System
 * Client-side helpers: form spinner, input validation feedback
 */

document.addEventListener("DOMContentLoaded", () => {

  // ── Prediction form: show spinner on submit ─────────────────
  const form      = document.getElementById("predictionForm");
  const btnText   = document.getElementById("btnText");
  const btnSpinner = document.getElementById("btnSpinner");
  const submitBtn = document.getElementById("submitBtn");

  if (form) {
    form.addEventListener("submit", (e) => {
      // Basic HTML5 validity check before showing spinner
      if (!form.checkValidity()) return;

      // Quick range checks to avoid pointless server round-trips
      const fields = [
        { id: "study_hours",           min: 0, max: 24  },
        { id: "attendance_percentage", min: 0, max: 100 },
        { id: "sleep_hours",           min: 0, max: 24  },
        { id: "previous_marks",        min: 0, max: 100 },
        { id: "assignments_completed", min: 0, max: 20  },
        { id: "screen_time",           min: 0, max: 24  },
      ];

      let hasError = false;
      fields.forEach(({ id, min, max }) => {
        const el  = document.getElementById(id);
        const val = parseFloat(el.value);
        if (isNaN(val) || val < min || val > max) {
          el.classList.add("is-invalid");
          hasError = true;
        } else {
          el.classList.remove("is-invalid");
        }
      });

      if (hasError) { e.preventDefault(); return; }

      // Show spinner
      if (btnText && btnSpinner) {
        btnText.classList.add("d-none");
        btnSpinner.classList.remove("d-none");
        submitBtn.disabled = true;
      }
    });

    // Live validation: remove error class when user fixes input
    form.querySelectorAll("input").forEach((input) => {
      input.addEventListener("input", () => {
        input.classList.remove("is-invalid");
      });
    });
  }

  // ── Navbar active link highlight on scroll (optional polish) ─
  // already handled server-side via Jinja endpoint checks

});
