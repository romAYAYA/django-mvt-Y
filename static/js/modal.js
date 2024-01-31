    document.addEventListener("DOMContentLoaded", function () {
        const toggleButtons = document.querySelectorAll('[data-modal-toggle]');
        const hideButtons = document.querySelectorAll('[data-modal-hide]');

        toggleButtons.forEach(button => {
            button.addEventListener('click', () => {
                const targetModalId = button.dataset.modalToggle;
                const targetModal = document.getElementById(targetModalId);

                if (targetModal) {
                    targetModal.classList.toggle('hidden');
                    targetModal.setAttribute('aria-hidden', targetModal.classList.contains('hidden'));
                }
            });
        });

        hideButtons.forEach(button => {
            button.addEventListener('click', () => {
                const targetModalId = button.dataset.modalHide;
                const targetModal = document.getElementById(targetModalId);

                if (targetModal) {
                    targetModal.classList.add('hidden');
                    targetModal.setAttribute('aria-hidden', true);
                }
            });
        });
    });