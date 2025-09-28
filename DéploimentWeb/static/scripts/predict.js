document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('image');
    const cloudImage = document.getElementById('cloud');

    fileInput.addEventListener('change', (event) => {
        if (event.target.files && event.target.files.length > 0) {
            const selectedFile = event.target.files[0];
            const reader = new FileReader();

            reader.onload = (e) => {
                cloudImage.src = e.target.result;
                
                /*Caman('#cloud', function () {
                    this.revert();

                    this.hue(-13);

                    this.saturation(-70);
                    this.brightness(-20);

                    this.contrast(30);

                    this.render();
                });
                */
            };

            reader.readAsDataURL(selectedFile);
        }
    });
});
