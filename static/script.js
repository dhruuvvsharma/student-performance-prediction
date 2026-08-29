document.addEventListener("DOMContentLoaded", function () {

    /* ==============================
       GET ELEMENTS
    ================================= */

    const form = document.getElementById("predictionForm");

    const readingScore =
        document.getElementById("reading_score");

    const writingScore =
        document.getElementById("writing_score");

    const predictButton =
        document.getElementById("predictButton");


    /* ==============================
       SCORE VALIDATION
    ================================= */

    function validateScore(input) {

        const value = Number(input.value);


        // Empty input
        if (input.value === "") {

            input.setCustomValidity("");

            return;
        }


        // Score must be between 0 and 100
        if (value < 0 || value > 100) {

            input.setCustomValidity(
                "Score must be between 0 and 100."
            );

        } else {

            input.setCustomValidity("");

        }
    }


    /* ==============================
       READING SCORE
    ================================= */

    readingScore.addEventListener("input", function () {

        validateScore(readingScore);

    });


    /* ==============================
       WRITING SCORE
    ================================= */

    writingScore.addEventListener("input", function () {

        validateScore(writingScore);

    });


    /* ==============================
       FORM SUBMISSION
    ================================= */

    form.addEventListener("submit", function () {

        // Validate both scores
        validateScore(readingScore);
        validateScore(writingScore);


        /*
         * If the form is valid,
         * change button state.
         */

        if (form.checkValidity()) {

            predictButton.disabled = true;

            predictButton.textContent = "Predicting...";

        }

    });

});